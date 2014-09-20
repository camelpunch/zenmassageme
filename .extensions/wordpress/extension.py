"""WordPress Extension

Downloads, installs and configures WordPress
"""
import os
import os.path
import logging
from build_pack_utils import utils


_log = logging.getLogger('wordpress')


DEFAULTS = utils.FormattedDict({
    'WORDPRESS_VERSION': '4.0',
    'WORDPRESS_PACKAGE': 'wordpress-{WORDPRESS_VERSION}.tar.gz',
    'WORDPRESS_HASH': '17479e0e61e7a4f7ff92d58b28e14b381f07cbaf',
    'WORDPRESS_URL': 'https://wordpress.org/{WORDPRESS_PACKAGE}'
})


# Extension Methods
def preprocess_commands(ctx):
    return ()


def service_commands(ctx):
    return {}


def service_environment(ctx):
    return {}


def compile(install):
    print 'Installing Wordpress %s' % DEFAULTS['WORDPRESS_VERSION']
    ctx = install.builder._ctx
    inst = install._installer
    workDir = os.path.join(ctx['TMPDIR'], 'wordpress')
    inst.install_binary_direct(
        DEFAULTS['WORDPRESS_URL'],
        DEFAULTS['WORDPRESS_HASH'],
        workDir,
        fileName=DEFAULTS['WORDPRESS_PACKAGE'],
        strip=True)
    (install.builder
        .move()
        .everything()
        .under('{BUILD_DIR}/htdocs')
        .into(workDir)
        .done())
    (install.builder
        .move()
        .everything()
        .under(workDir)
        .into('{BUILD_DIR}/htdocs')
        .done())
    return 0
