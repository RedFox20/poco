import mama

##
# Explore Mama docs at https://github.com/RedFox20/Mama
#
class poco(mama.BuildTarget):

    def dependencies(self):
        pass

    def configure(self):
        self.add_cmake_options('POCO_STATIC=ON', 'POCO_MT=ON', 'ENABLE_MSVC_MP=ON',
            'ENABLE_DATA_MYSQL=OFF', 'ENABLE_DATA_POSTGRESQL=OFF',
            'ENABLE_DATA_ODBC=OFF', 'ENABLE_XML=OFF' 'ENABLE_MONGODB=OFF', 'ENABLE_DATA_SQLITE=OFF',
            'ENABLE_REDIS=OFF', 'ENABLE_SEVENZIP=OFF' 'ENABLE_ZIP=OFF', 'ENABLE_CPPPARSER=OFF',
            'ENABLE_PAGECOMPILER=OFF', 'ENABLE_PAGECOMPILER_FILE2PAGE=OFF' 'ENABLE_TESTS=OFF',
            'ENABLE_CRYPTO=OFF', 'ENABLE_APACHECONNECTOR=OFF', 'ENABLE_UTIL=OFF')

    def package(self):
        self.export_include('include', build_dir=True)
        self.export_libs('lib', ['.lib','.a'], order=[
            'PocoUtil', 'PocoNet', 'PocoJSON', 'PocoXML', 'PocoEncodings', 'PocoFoundation'
        ])
