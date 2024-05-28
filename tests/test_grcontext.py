import skia
import pytest
from datetime import timedelta


@pytest.fixture
def backend_semaphore():
    return skia.GrBackendSemaphore()


def test_GrBackendSemaphore_initGL(backend_semaphore):
    backend_semaphore.initGL(None)


def test_GrBackendSemaphore_initVulkan(backend_semaphore):
    backend_semaphore.initVulkan(None)


def test_GrBackendSemaphore_isInitialized(backend_semaphore):
    assert isinstance(backend_semaphore.isInitialized(), bool)


def test_GrBackendSemaphore_glSync(backend_semaphore):
    backend_semaphore.glSync()


def test_GrBackendSemaphore_vkSemaphore(backend_semaphore):
    backend_semaphore.vkSemaphore()


@pytest.fixture(scope='module')
def backend_format():
    return skia.GrBackendFormat.MakeMock(
            skia.GrColorType.kBGRA_8888, skia.Image.kBC1_RGBA8_UNORM)


def test_GrBackendFormat_MakeGL():
    assert isinstance(skia.GrBackendFormat.MakeGL(0, 0), skia.GrBackendFormat)


def test_GrBackendFormat_MakeVk_1():
    assert isinstance(
        skia.GrBackendFormat.MakeVk(0), (type(None), skia.GrBackendFormat))


def test_GrBackendFormat_MakeVk_2():
    assert isinstance(
        skia.GrBackendFormat.MakeVk(skia.GrVkYcbcrConversionInfo()),
        (type(None), skia.GrBackendFormat))


def test_GrBackendFormat_MakeMock(backend_format):
    assert isinstance(backend_format, skia.GrBackendFormat)


def test_GrBackendFormat_eq(backend_format):
    assert backend_format == backend_format


def test_GrBackendFormat_ne(backend_format):
    assert backend_format != skia.GrBackendFormat()


def test_GrBackendFormat_backend(backend_format):
    assert isinstance(backend_format.backend(), skia.GrBackendApi)


def test_GrBackendFormat_textureType(backend_format):
    assert isinstance(backend_format.textureType(), skia.GrTextureType)


def test_GrBackendFormat_channelMask(backend_format):
    assert isinstance(backend_format.channelMask(), int)


def test_GrBackendFormat_asVkFormat(backend_format):
    fmt = 1
    assert isinstance(backend_format.asVkFormat(fmt), bool)


def test_GrBackendFormat_asGLFormat(backend_format):
    assert isinstance(backend_format.asGLFormat(), skia.GrGLFormat)


def test_GrBackendFormat_getVkYcbcrConversionInfo(backend_format):
    assert isinstance(
        backend_format.getVkYcbcrConversionInfo(),
        (type(None), skia.GrVkYcbcrConversionInfo))


def test_GrBackendFormat_isValid(backend_format):
    assert isinstance(backend_format.isValid(), bool)


@pytest.fixture(scope='module')
def backend_texture(context, gl_texture_info):
    return skia.GrBackendTexture(
        256, 256, skia.GrMipmapped.kNo, gl_texture_info)


def test_GrBackendTexture_init_glInfo(gl_texture_info):
    assert isinstance(
        skia.GrBackendTexture(128, 128, skia.GrMipmapped.kNo, gl_texture_info),
        skia.GrBackendTexture)


def test_GrBackendTexture_init_mockInfo(mock_texture_info):
    assert isinstance(
        skia.GrBackendTexture(
            128, 128, skia.GrMipmapped.kNo, mock_texture_info),
        skia.GrBackendTexture)


def test_GrBackendTexture_dimensions(backend_texture):
    assert isinstance(backend_texture.dimensions(), skia.ISize)


def test_GrBackendTexture_width(backend_texture):
    assert isinstance(backend_texture.width(), int)


def test_GrBackendTexture_height(backend_texture):
    assert isinstance(backend_texture.height(), int)


def test_GrBackendTexture_hasMipmaps(backend_texture):
    assert isinstance(backend_texture.hasMipmaps(), bool)


def test_GrBackendTexture_getGLTextureInfo(backend_texture, gl_texture_info):
    assert isinstance(backend_texture.getGLTextureInfo(gl_texture_info), bool)


def test_GrBackendTexture_glTextureParametersModified(backend_texture):
    backend_texture.glTextureParametersModified()


def test_GrBackendTexture_getBackendFormat(backend_texture):
    assert isinstance(backend_texture.getBackendFormat(), skia.GrBackendFormat)


def test_GrBackendTexture_getMockTextureInfo(
    backend_texture, mock_texture_info):
    assert isinstance(
        backend_texture.getMockTextureInfo(mock_texture_info), bool)


def test_GrBackendTexture_isProtected(backend_texture):
    assert isinstance(backend_texture.isProtected(), bool)


def test_GrBackendTexture_isValid(backend_texture):
    assert isinstance(backend_texture.isValid(), bool)


def test_GrBackendTexture_isSameTexture(backend_texture):
    assert isinstance(backend_texture.isSameTexture(backend_texture), bool)


@pytest.fixture
def grflushinfo():
    return skia.GrFlushInfo()


def test_GrFlushInfo_fNumSemaphores(grflushinfo):
    assert isinstance(grflushinfo.fNumSemaphores, int)


def test_GrFlushInfo_semaphores(grflushinfo, backend_semaphore):
    grflushinfo.semaphores = [backend_semaphore]
    assert isinstance(grflushinfo.semaphores, list)


@pytest.fixture
def backend_render_target():
    return skia.GrBackendRenderTarget()


@pytest.mark.parametrize('args', [
    tuple(),
    (128, 128, 2, 8, skia.GrGLFramebufferInfo()),
    # (128, 128, 2, 8, skia.GrVkImageInfo()),
    (128, 128, 2, 8, skia.GrMockRenderTargetInfo()),
])
def test_GrBackendRenderTarget_init(args):
    assert isinstance(
        skia.GrBackendRenderTarget(*args), skia.GrBackendRenderTarget)


def test_GrBackendRenderTarget_dimensions(backend_render_target):
    assert isinstance(backend_render_target.dimensions(), skia.ISize)


def test_GrBackendRenderTarget_width(backend_render_target):
    assert isinstance(backend_render_target.width(), int)


def test_GrBackendRenderTarget_height(backend_render_target):
    assert isinstance(backend_render_target.height(), int)


def test_GrBackendRenderTarget_sampleCnt(backend_render_target):
    assert isinstance(backend_render_target.sampleCnt(), int)


def test_GrBackendRenderTarget_stencilBits(backend_render_target):
    assert isinstance(backend_render_target.stencilBits(), int)


def test_GrBackendRenderTarget_backend(backend_render_target):
    assert isinstance(backend_render_target.backend(), skia.GrBackendApi)


def test_GrBackendRenderTarget_isFramebufferOnly(backend_render_target):
    assert isinstance(backend_render_target.isFramebufferOnly(), bool)


def test_GrBackendRenderTarget_getGLFramebufferInfo(backend_render_target):
    info = skia.GrGLFramebufferInfo()
    assert isinstance(backend_render_target.getGLFramebufferInfo(info), bool)


def test_GrBackendRenderTarget_getVkImageInfo(backend_render_target):
    info = skia.GrVkImageInfo()
    assert isinstance(backend_render_target.getVkImageInfo(info), bool)


def test_GrBackendRenderTarget_setVkImageLayout(backend_render_target):
    backend_render_target.setVkImageLayout(0)


def test_GrBackendRenderTarget_getBackendFormat(backend_render_target):
    assert isinstance(
        backend_render_target.getBackendFormat(), skia.GrBackendFormat)


def test_GrBackendRenderTarget_getMockRenderTargetInfo(backend_render_target):
    info = skia.GrMockRenderTargetInfo()
    assert isinstance(backend_render_target.getMockRenderTargetInfo(info), bool)


def test_GrBackendRenderTarget_isProtected(backend_render_target):
    assert isinstance(backend_render_target.isProtected(), bool)


def test_GrBackendRenderTarget_isValid(backend_render_target):
    assert isinstance(backend_render_target.isValid(), bool)


@pytest.fixture
def backend_surface_mutable_state():
    return skia.GrBackendSurfaceMutableState()


def test_GrBackendSurfaceMutableState_init(backend_surface_mutable_state):
    assert isinstance(
        backend_surface_mutable_state, skia.GrBackendSurfaceMutableState)


def test_GrBackendSurfaceMutableState_isValid(backend_surface_mutable_state):
    assert isinstance(backend_surface_mutable_state.isValid(), bool)


def test_GrBackendSurfaceMutableState_isValid(backend_surface_mutable_state):
    assert isinstance(
        backend_surface_mutable_state.backend(), skia.GrBackendApi)


def test_GrContext_resetContext(context):
    context.resetContext()


def test_GrContext_resetGLTextureBindings(context):
    context.resetGLTextureBindings()


@pytest.mark.skip(reason='This destroys the context')
def test_GrContext_abandonContext(context):
    context.abandonContext()


def test_GrRecordingContext_abandoned(context):
    assert isinstance(context.abandoned(), bool)


def test_GrContext_oomed(context):
    assert isinstance(context.oomed(), bool)


@pytest.mark.skip(reason='This destroys the context')
def test_GrContext_releaseResourcesAndAbandonContext(context):
    context.releaseResourcesAndAbandonContext()


def test_GrContext_getResourceCacheLimit(context):
    assert isinstance(context.getResourceCacheLimit(), int)


def test_GrContext_getResourceCacheUsage(context):
    resource_count, max_resource_bytes = 0, 0
    context.getResourceCacheUsage(resource_count, max_resource_bytes)


def test_GrContext_getResourceCachePurgeableBytes(context):
    assert isinstance(context.getResourceCachePurgeableBytes(), int)


def test_GrContext_setResourceCacheLimit(context):
    context.setResourceCacheLimit((1 << 16))


def test_GrContext_freeGpuResources(context):
    context.freeGpuResources()


def test_GrContext_performDeferredCleanup(context):
    context.performDeferredCleanup(timedelta(milliseconds=1000))


def test_GrContext_purgeResourcesNotUsedInMs(context):
    context.purgeResourcesNotUsedInMs(timedelta(milliseconds=1000))


@pytest.mark.parametrize('args', [
    (1 << 16, True),
    (True,),
])
def test_GrContext_purgeUnlockedResources(context, args):
    context.purgeUnlockedResources(*args)


def test_GrContext_maxTextureSize(context):
    assert isinstance(context.maxTextureSize(), int)


def test_GrContext_maxRenderTargetSize(context):
    assert isinstance(context.maxRenderTargetSize(), int)


def test_GrContext_colorTypeSupportedAsImage(context):
    assert isinstance(context.colorTypeSupportedAsImage(
        skia.ColorType.kRGBA_8888_ColorType), bool)


def test_GrContext_colorTypeSupportedAsSurface(context):
    assert isinstance(context.colorTypeSupportedAsSurface(
        skia.ColorType.kRGBA_8888_ColorType), bool)


def test_GrContext_maxSurfaceSampleCountForColorType(context):
    assert isinstance(context.maxSurfaceSampleCountForColorType(
        skia.ColorType.kRGBA_8888_ColorType), int)


def test_GrContext_wait(context, backend_semaphore):
    assert isinstance(context.wait([backend_semaphore]), bool)


def test_GrContext_flush(context, grflushinfo):
    assert isinstance(context.flush(grflushinfo), skia.GrSemaphoresSubmitted)


def test_GrContext_flushAndSubmit(context):
    context.flushAndSubmit()


def test_GrContext_submit(context):
    context.submit()


def test_GrContext_checkAsyncWorkCompletion(context):
    context.checkAsyncWorkCompletion()


def test_GrContext_supportsDistanceFieldText(context):
    assert isinstance(context.supportsDistanceFieldText(), bool)


def test_GrContext_storeVkPipelineCacheData(context):
    context.storeVkPipelineCacheData()


def test_GrRecordingContext_defaultBackendFormat(context):
    assert isinstance(
        context.defaultBackendFormat(
            skia.ColorType.kRGBA_8888_ColorType, skia.GrRenderable.kNo),
        skia.GrBackendFormat)


def test_GrRecordingContext_maxTextureSize(context):
    assert isinstance(context.maxTextureSize(), int)


def test_GrRecordingContext_maxRenderTargetSize(context):
    assert isinstance(context.maxRenderTargetSize(), int)


def test_GrRecordingContext_colorTypeSupportedAsImage(context):
    assert isinstance(
        context.colorTypeSupportedAsImage(skia.kRGBA_8888_ColorType), bool)


@pytest.mark.parametrize('args', [
    (64, 64, skia.GrBackendFormat(), skia.GrMipmapped.kNo,
        skia.GrRenderable.kNo),
    (64, 64, skia.ColorType.kRGBA_8888_ColorType, skia.GrMipmapped.kNo,
        skia.GrRenderable.kNo),
    (64, 64, skia.GrBackendFormat(), 0xFFFFFFFF, skia.GrMipmapped.kNo,
        skia.GrRenderable.kNo),
    (64, 64, skia.ColorType.kRGBA_8888_ColorType, 0xFFFFFFFF,
        skia.GrMipmapped.kNo, skia.GrRenderable.kNo),
])
def test_GrContext_createBackendTexture(context, args, request):
    backend_texture = context.createBackendTexture(*args)
    assert isinstance(backend_texture, skia.GrBackendTexture)
    context.deleteBackendTexture(backend_texture)


def test_GrContext_createBackendTexture_2(context, pixmap):
    backend_texture = context.createBackendTexture(
        [pixmap], skia.GrRenderable.kNo)
    assert isinstance(backend_texture, skia.GrBackendTexture)
    context.deleteBackendTexture(backend_texture)


def test_GrContext_createBackendTexture_3(context, pixmap):
    backend_texture = context.createBackendTexture(
        pixmap, skia.GrRenderable.kNo)
    assert isinstance(backend_texture, skia.GrBackendTexture)
    context.deleteBackendTexture(backend_texture)


def test_GrContext_updateBackendTexture_1(context):
    backend_texture = context.createBackendTexture(
        64, 64, skia.ColorType.kRGBA_8888_ColorType, 0xFFFFFFFF,
        skia.GrMipmapped.kNo, skia.GrRenderable.kNo)
    assert isinstance(
        context.updateBackendTexture(backend_texture, skia.ColorBLACK), bool)
    context.deleteBackendTexture(backend_texture)


def test_GrContext_updateBackendTexture_2(context, pixmap):
    backend_texture = context.createBackendTexture(
        64, 64, skia.ColorType.kRGBA_8888_ColorType, 0xFFFFFFFF,
        skia.GrMipmapped.kNo, skia.GrRenderable.kNo)
    assert isinstance(
        context.updateBackendTexture(backend_texture, [pixmap]), bool)
    context.deleteBackendTexture(backend_texture)


def test_GrContext_compressedBackendFormat(context):
    assert isinstance(
        context.compressedBackendFormat(skia.Image.kBC1_RGBA8_UNORM),
        skia.GrBackendFormat)


@pytest.mark.parametrize('args', [
    (64, 64, skia.GrBackendFormat(), 0xFFFFFFFF, skia.GrMipmapped.kNo),
    (64, 64, skia.Image.kBC1_RGBA8_UNORM, 0xFFFFFFFF, skia.GrMipmapped.kNo),
    (16, 16, skia.GrBackendFormat(), bytearray(256), skia.GrMipmapped.kNo),
    (16, 16, skia.Image.kBC1_RGBA8_UNORM, bytearray(256), skia.GrMipmapped.kNo),
])
def test_GrContext_createCompressedBackendTexture(context, args):
    backend_texture = context.createCompressedBackendTexture(*args)
    assert isinstance(backend_texture, skia.GrBackendTexture)
    context.deleteBackendTexture(backend_texture)


@pytest.mark.skip("Vulkan not supported")
def test_GrContext_setBackendTextureState(context, backend_texture):
    state = skia.GrBackendSurfaceMutableState()
    assert isinstance(
        context.setBackendTextureState(backend_texture, state), bool)


@pytest.mark.skip("Vulkan not supported")
def test_GrContext_setBackendRenderTargetState(context, backend_render_target):
    state = skia.GrBackendSurfaceMutableState()
    assert isinstance(
        context.setBackendRenderTargetState(backend_render_target, state), bool)


# def test_GrContext_deleteBackendTexture(context):
#     pass


@pytest.mark.skip()
def test_GrContext_precompileShader(context):
    assert isinstance(context.precompileShader(b'', b''), bool)


def test_GrContext_ComputeImageSize(image):
    assert isinstance(
        skia.GrContext.ComputeImageSize(image, skia.GrMipmapped.kYes),
        int)


def test_GrDirectContext_MakeGL(context):
    assert isinstance(context, skia.GrDirectContext)


@pytest.mark.skip(reason='Vulkan not supported yet.')
def test_GrDirectContext_MakeVulkan():
    context = skia.GrVkBackendContext()
    options = skia.GrContextOptions()
    assert isinstance(
        skia.GrDirectContext.MakeVulkan(context),
        (type(None), skia.GrDirectContext))
    assert isinstance(
        skia.GrDirectContext.MakeVulkan(context, options),
        (type(None), skia.GrDirectContext))


def test_GrDirectContext_MakeMock():
    assert isinstance(
        skia.GrDirectContext.MakeMock(
            skia.GrMockOptions(), skia.GrContextOptions()),
        skia.GrDirectContext)


@pytest.fixture(scope='module')
def gl_texture_info():
    return skia.GrGLTextureInfo()


def test_GrGLTextureInfo_init(gl_texture_info):
    assert isinstance(gl_texture_info, skia.GrGLTextureInfo)


@pytest.fixture(scope='module')
def mock_texture_info():
    return skia.GrMockTextureInfo()


def test_GrMockTextureInfo_init(mock_texture_info):
    assert isinstance(mock_texture_info, skia.GrMockTextureInfo)


@pytest.fixture(scope='module')
def mock_render_target_info():
    return skia.GrMockRenderTargetInfo()


def test_GrMockRenderTargetInfo_init(mock_render_target_info):
    assert isinstance(mock_render_target_info, skia.GrMockRenderTargetInfo)


@pytest.fixture(scope='module')
def gl_framebuffer_info():
    return skia.GrGLFramebufferInfo()


def test_GrGLFramebufferInfo_init(gl_framebuffer_info):
    assert isinstance(gl_framebuffer_info, skia.GrGLFramebufferInfo)


def test_GrVkImageInfo_init():
    assert isinstance(skia.GrVkImageInfo(), skia.GrVkImageInfo)


def test_GrVkBackendContext_init():
    assert isinstance(skia.GrVkBackendContext(), skia.GrVkBackendContext)

@pytest.mark.xfail(reason='This is expected to fail with the import')
def test_ShaderError():
    import glfw
    from OpenGL import GL # github CI 3.7 fails dlopen() here.

    path = skia.Path()
    path.moveTo(184, 445)
    path.lineTo(249, 445)
    path.quadTo(278, 445, 298, 438)
    path.quadTo(318, 431, 331, 419)
    path.quadTo(344, 406, 350, 390)
    path.quadTo(356, 373, 356, 354)
    path.quadTo(356, 331, 347, 312)
    path.quadTo(338, 292, 320, 280) # <- comment out this line and shape will draw correctly with anti-aliasing
    path.close()

    if not glfw.init():
        raise RuntimeError('glfw.init() failed')
    glfw.window_hint(glfw.VISIBLE, glfw.FALSE)
    glfw.window_hint(glfw.STENCIL_BITS, 8)
    # See https://www.glfw.org/faq#macos
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 2)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, True)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
    window = glfw.create_window(640, 480, '', None, None)
    assert window is not None
    glfw.make_context_current(window)

    context = skia.GrDirectContext.MakeGL()
    assert context is not None                                # assert here
    (fb_width, fb_height) = glfw.get_framebuffer_size(window) # segfault against 3.9, 3.11
    backend_render_target = skia.GrBackendRenderTarget(
        fb_width,
        fb_height,
        0,  # sampleCnt
        0,  # stencilBits
        skia.GrGLFramebufferInfo(0, GL.GL_RGBA8))
    surface = skia.Surface.MakeFromBackendRenderTarget(
        context, backend_render_target, skia.kBottomLeft_GrSurfaceOrigin,
        skia.kRGBA_8888_ColorType, skia.ColorSpace.MakeSRGB())
    assert surface is not None                                # assert here, with stderr "nullptr GL version string."
    # cp311-macosx_x86_64/venv-test/lib/python3.11/site-packages/glfw/__init__.py:914: GLFWError: (65545) b'NSGL: Failed to find a suitable pixel format'
    #     warnings.warn(message, GLFWError)

    GL.glClear(GL.GL_COLOR_BUFFER_BIT)

    with surface as canvas:
        canvas.drawCircle(100, 100, 40, skia.Paint(Color=skia.ColorGREEN, AntiAlias=True))

        paint = skia.Paint(Color=skia.ColorBLUE)
        paint.setStyle(skia.Paint.kStroke_Style)
        paint.setStrokeWidth(2)
        paint.setAntiAlias(True)

        canvas.drawPath(path, paint)

    surface.flushAndSubmit()
    import glfw
    glfw.swap_buffers(window)

def test_ShaderError_2():
    from OpenGL.GLUT import glutInit, glutInitDisplayMode, GLUT_DOUBLE, GLUT_RGBA, glutInitWindowSize, glutCreateWindow, \
        glutSwapBuffers, glutPostRedisplay, glutDisplayFunc, glutMainLoop, glutMainLoopEvent, glutInitContextVersion, glutInitContextProfile, GLUT_CORE_PROFILE, glutHideWindow
    from OpenGL.GL import glClear, GL_COLOR_BUFFER_BIT, GL_DEPTH_BUFFER_BIT, GL_RGBA8, \
         glGetString, GL_VENDOR, GL_RENDERER, GL_VERSION, GL_SHADING_LANGUAGE_VERSION
    import sys
    if sys.platform.startswith("darwin"):
        # glutMainLoopEvent is a Linux/freeglut extension, and glutCheckLoop is an Apple one.
        ## Apparently glutCheckLoop will block (According to https://groups.google.com/g/glumpy-users/c/SiolfYO1zCA)
        ## and typically used with:
        ##     stop = False
        ##     ...
        ##     global stop
        ##     while not stop:
        ##         glut.glutCheckLoop()
        from OpenGL.GLUT import glutCheckLoop as glutMainLoopEvent

    path = skia.Path()
    path.moveTo(184, 445)
    path.lineTo(249, 445)
    path.quadTo(278, 445, 298, 438)
    path.quadTo(318, 431, 331, 419)
    path.quadTo(344, 406, 350, 390)
    path.quadTo(356, 373, 356, 354)
    path.quadTo(356, 331, 347, 312)
    path.quadTo(338, 292, 320, 280) # <- comment out this line and shape will draw correctly with anti-aliasing
    path.close()

    glutInit()
    if not sys.platform.startswith("darwin"):
        glutInitContextVersion(4, 1)
        glutInitContextProfile(GLUT_CORE_PROFILE)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowSize(600, 480)
    glutCreateWindow(b"OpenGL Window")
    glutHideWindow()

    context = skia.GrDirectContext.MakeGL()

    import warnings
    print(glGetString(GL_VENDOR).decode())
    print(glGetString(GL_RENDERER).decode())
    print(glGetString(GL_VERSION).decode())
    print(glGetString(GL_SHADING_LANGUAGE_VERSION).decode())
    warnings.warn(UserWarning('"%s"' % glGetString(GL_VENDOR).decode()))
    warnings.warn(UserWarning('"%s"' % glGetString(GL_RENDERER).decode()))
    warnings.warn(UserWarning('"%s"' % glGetString(GL_VERSION).decode()))
    warnings.warn(UserWarning('"%s"' % glGetString(GL_SHADING_LANGUAGE_VERSION).decode()))
#    assert (glGetString(GL_VENDOR) == b'AMD' and
#            glGetString(GL_RENDERER) == b'AMD Radeon R5 Graphics (radeonsi, stoney, LLVM 18.1.1, DRM 3.57, 6.8.9-300.fc40.x86_64)' and
#            glGetString(GL_VERSION) == b'4.5 (Compatibility Profile) Mesa 24.0.7' and
#            glGetString(GL_SHADING_LANGUAGE_VERSION) == b'4.50')

    backend_render_target = skia.GrBackendRenderTarget(
        600,
        480,
        0,  # sampleCnt
        0,  # stencilBits
        skia.GrGLFramebufferInfo(0, GL_RGBA8))
    surface = skia.Surface.MakeFromBackendRenderTarget(
        context, backend_render_target, skia.kBottomLeft_GrSurfaceOrigin,
        skia.kRGBA_8888_ColorType, skia.ColorSpace.MakeSRGB())
    assert surface is not None

    def display():
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        with surface as canvas:
            canvas.drawCircle(100, 100, 40, skia.Paint(Color=skia.ColorGREEN, AntiAlias=True))

            paint = skia.Paint(Color=skia.ColorBLUE)
            paint.setStyle(skia.Paint.kStroke_Style)
            paint.setStrokeWidth(2)
        paint.setAntiAlias(True)

        canvas.drawPath(path, paint)

    surface.flushAndSubmit()
    glutSwapBuffers()
    glutPostRedisplay()
    glutDisplayFunc(display)
    #glutMainLoop()
    ## Apple's glutCheckLoop seems to just quit and die...
    display()
    import time
    time.sleep(3)
    #glutMainLoopEvent() # paint once then exit
