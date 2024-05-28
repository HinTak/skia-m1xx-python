import contextlib
import skia
import os
import pytest
import sys
import logging

logger = logging.getLogger(__name__)


from OpenGL.GL import glGetString, GL_VENDOR, GL_RENDERER, GL_VERSION, GL_SHADING_LANGUAGE_VERSION
import warnings


@pytest.fixture(scope='session')
def glfw_context():
    import glfw
    if not glfw.init():
        raise RuntimeError('glfw.init() failed')
    glfw.window_hint(glfw.VISIBLE, glfw.FALSE)
    glfw.window_hint(glfw.STENCIL_BITS, 8)
    # see https://www.glfw.org/faq#macos
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 2)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, True)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
    context = glfw.create_window(640, 480, '', None, None)
    glfw.make_context_current(context)
    logger.debug('glfw context created')
    yield context
    glfw.destroy_window(context)
    glfw.terminate()


@pytest.fixture(scope='session')
def glut_context():
    from OpenGL.GLUT import glutInit, glutCreateWindow, glutHideWindow, glutInitContextVersion, glutInitContextProfile, GLUT_CORE_PROFILE
    glutInit()
    if not sys.platform.startswith("darwin"):
        glutInitContextVersion(4, 1)
        glutInitContextProfile(GLUT_CORE_PROFILE)
    context = glutCreateWindow('Hidden window for OpenGL context')
    glutHideWindow()
    logger.debug('glut context created')
    yield context


@pytest.fixture(scope='session')
def opengl_context(request):
    try:
        yield request.getfixturevalue('glfw_context')
        return
    except ImportError:
        warnings.warn(UserWarning('glfw not found'))
        logger.warning('glfw not found')
    except UserWarning as e:
        logger.exception(e)
        warnings.warn(e)
        pytest.skip('GLFW error')

    try:
        yield request.getfixturevalue('glut_context')
    except ImportError:
        warnings.warn(UserWarning('pyopengl not found'))
        logger.warning('pyopengl not found')

    pytest.skip('OpenGL is not available')


@pytest.fixture(scope='session')
def context(opengl_context):
    context = skia.GrDirectContext.MakeGL()
    if not isinstance(context, skia.GrContext):
        warnings.warn(UserWarning('Failed to create GrDirectContext'))
        pytest.skip('Failed to create GrDirectContext')
    else:
        warnings.warn(UserWarning('"%s"' % glGetString(GL_VENDOR).decode()))
        warnings.warn(UserWarning('"%s"' % glGetString(GL_RENDERER).decode()))
        warnings.warn(UserWarning('"%s"' % glGetString(GL_VERSION).decode()))
        warnings.warn(UserWarning('"%s"' % glGetString(GL_SHADING_LANGUAGE_VERSION).decode()))
    yield context


@pytest.fixture(scope='module', params=['raster', 'gpu'])
def surface(request):
    if request.param == 'gpu':
        context = request.getfixturevalue('context')
        info = skia.ImageInfo.MakeN32Premul(320, 240)
        return skia.Surface.MakeRenderTarget(
            context, skia.Budgeted.kNo, info)
    else:
        return skia.Surface(320, 240)


@pytest.fixture
def canvas(surface):
    canvas = surface.getCanvas()
    yield canvas
    canvas.clear(skia.ColorWHITE)
    canvas.flush()


@pytest.fixture(scope='session')
def resource_path():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(root_dir, 'skia', 'resources')


@pytest.fixture(scope='session')
def png_path(resource_path):
    return os.path.join(resource_path, 'images', 'color_wheel.png')


@pytest.fixture(scope='session')
def png_data(png_path):
    return skia.Data.MakeFromFileName(png_path)


@pytest.fixture(scope='session')
def image(png_data):
    return skia.Image.MakeFromEncoded(png_data)


@pytest.fixture(scope='module')
def picture():
    recorder = skia.PictureRecorder()
    canvas = recorder.beginRecording(skia.Rect(100, 100))
    canvas.clear(0xFFFFFFFF)
    canvas.drawLine(0, 0, 100, 100, skia.Paint())
    return recorder.finishRecordingAsPicture()


@pytest.fixture
def pixmap():
    info = skia.ImageInfo.MakeN32Premul(100, 100)
    data = bytearray(info.computeMinByteSize())
    yield skia.Pixmap(info, data, info.minRowBytes())


@pytest.fixture
def vertices():
    return skia.Vertices(
        skia.Vertices.kTriangles_VertexMode,
        [skia.Point(0, 0), skia.Point(1, 1), skia.Point(1, 0)],
        [skia.Point(1, 1), skia.Point(1, 0), skia.Point(0, 0)],
        [skia.ColorRED, skia.ColorRED, skia.ColorRED],
    )


@pytest.fixture(scope='session')
def ttf_path(resource_path):
    return os.path.join(resource_path, 'fonts', 'Distortable.ttf')
