{
    "targets": [{
        "target_name": "lwip_encoder",
        "sources": [
            # LWIP:
            #######
            "src/encoder/init.cpp",
            "src/encoder/jpeg_worker.cpp",
            "src/encoder/png_worker.cpp",
            "src/encoder/gif_worker.cpp",
            # LIB JPEG:
            ###########
            "src/lib/jpeg/jdatadst.c",
            "src/lib/jpeg/jmemnobs.c",
            "src/lib/jpeg/jcomapi.c",
            "src/lib/jpeg/jerror.c",
            "src/lib/jpeg/jfdctflt.c",
            "src/lib/jpeg/jfdctfst.c",
            "src/lib/jpeg/jfdctint.c",
            "src/lib/jpeg/jidctflt.c",
            "src/lib/jpeg/jidctfst.c",
            "src/lib/jpeg/jidctint.c",
            "src/lib/jpeg/jutils.c",
            "src/lib/jpeg/jmemmgr.c",
            "src/lib/jpeg/jaricom.c",
            "src/lib/jpeg/jquant1.c",
            "src/lib/jpeg/jquant2.c",
            "src/lib/jpeg/jcapimin.c",
            "src/lib/jpeg/jcapistd.c",
            "src/lib/jpeg/jccoefct.c",
            "src/lib/jpeg/jccolor.c",
            "src/lib/jpeg/jcdctmgr.c",
            "src/lib/jpeg/jchuff.c",
            "src/lib/jpeg/jcinit.c",
            "src/lib/jpeg/jcmainct.c",
            "src/lib/jpeg/jcmarker.c",
            "src/lib/jpeg/jcmaster.c",
            "src/lib/jpeg/jcparam.c",
            "src/lib/jpeg/jcprepct.c",
            "src/lib/jpeg/jcsample.c",
            "src/lib/jpeg/jcarith.c",
            # LIB PNG:
            ##########
            "src/lib/png/png.c",
            "src/lib/png/pngset.c",
            "src/lib/png/pngget.c",
            "src/lib/png/pngtrans.c",
            "src/lib/png/pngmem.c",
            "src/lib/png/pngerror.c",
            "src/lib/png/pngwrite.c",
            "src/lib/png/pngwutil.c",
            "src/lib/png/pngwio.c",
            "src/lib/png/pngwtran.c",
            # ZLIB:
            #######
            "src/lib/zlib/adler32.c",
            "src/lib/zlib/crc32.c",
            "src/lib/zlib/gzlib.c",
            "src/lib/zlib/zutil.c",
            "src/lib/zlib/gzwrite.c",
            "src/lib/zlib/compress.c",
            "src/lib/zlib/deflate.c",
            "src/lib/zlib/trees.c",
            # LIB GIF:
            ##########
            "src/lib/gif/egif_lib.c",
            "src/lib/gif/gif_err.c",
            "src/lib/gif/gifalloc.c",
            "src/lib/gif/gif_hash.c",
            "src/lib/gif/quantize.c"
        ],
        'include_dirs': [
            '<!(node -e "require(\'nan\')")',
            'src/encoder',
            'src/lib/zlib',
            'src/lib/jpeg',
            'src/lib/cimg',
            'src/lib/png',
            'src/lib/gif'
        ],
        'conditions': [
            ['OS=="freebsd"', {
                'cflags!': ['-fno-exceptions'],
                'cflags_cc!': ['-fno-exceptions'],
            }],
            ['OS=="solaris"', {
                'cflags!': ['-fno-exceptions'],
                'cflags_cc!': ['-fno-exceptions'],
            }],
            ['OS=="linux"', {
                'cflags!': ['-fno-exceptions'],
                'cflags_cc!': ['-fno-exceptions'],
            }],
            ['OS=="mac"', {
                'xcode_settings': {
                    'GCC_ENABLE_CPP_EXCEPTIONS': 'YES'
                },
                'include_dirs': ['/usr/include/malloc']
            }],
            ['OS=="win"', {
                'configurations': {
                    'Release': {
                        'msvs_settings': {
                            'VCCLCompilerTool': {
                                'ExceptionHandling': 1
                            }
                        }
                    }
                },
                'include_dirs': ['src/win']
            }]
        ]
    },
    {
      "target_name": "action_after_build",
      "type": "none",
      "dependencies": [ "<(module_name)" ],
      "copies": [
        {
          "files": [ "<(PRODUCT_DIR)/<(module_name).node" ],
          "destination": "<(module_path)"
        }
      ]
    }]
}
