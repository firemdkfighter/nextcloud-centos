Name:           nextcloud
Version:        24.0.2
Release:        1%{?dist}
Summary:        Private file sync and share server
License:        AGPLv3+ and MIT and BSD and ASL 2.0 and WTFPL and CC-BY-SA and GPLv3+ and Adobe
URL:            http://nextcloud.com
Source0:        https://download.nextcloud.com/server/releases/%{name}-%{version}.tar.bz2

# basic nextcloud config.php, nextcloud's
# initial setup will fill out other settings appropriately
Source1:        %{name}-config.php
# Systemd timer for background jobs
Source2:       %{name}-systemd-timer.service
Source3:       %{name}-systemd-timer.timer
# httpd config files
Source100:      %{name}-httpd.conf
Source101:      %{name}-access-httpd.conf.avail
Source102:      %{name}-auth-any.inc
Source103:      %{name}-auth-local.inc
Source104:      %{name}-auth-none.inc
Source105:      %{name}-defaults.inc
# nginx/php-fpm  config files
Source200:      %{name}-default-nginx.conf
Source201:      %{name}-conf-nginx.conf
Source202:      %{name}-php-fpm.conf
# packaging notes and doc
Source300:      %{name}-README.fedora
Source301:      %{name}-mysql.txt
Source302:      %{name}-postgresql.txt
Source303:      %{name}-MIGRATION.fedora

# Remove updater version check, we know that updates across more than one
# version are possible
Patch0:         0000-disable-update-version-check.patch
# Change occ shebang to /usr/bin/php
Patch1:         0001-mangle-shebang.patch

BuildArch:      noarch
# For the systemd macros
%if 0%{?fedora} > 29
BuildRequires:  systemd-rpm-macros
%else
BuildRequires:  systemd
%endif
# expand pear macros on install
BuildRequires:  php-pear

# Require one webserver and database backend
Requires:       %{name}-webserver = %{version}-%{release}
Requires:       %{name}-database = %{version}-%{release}
# Require php CLI for occ command
Requires:       php-cli
# Core PHP libs/extensions required by OC core
Requires:       php-curl
Requires:       php-dom
Requires:       php-exif
Requires:       php-fileinfo
Requires:       php-gd
Requires:       php-iconv
Requires:       php-json
Requires:       php-ldap
Requires:       php-mbstring
Requires:       php-openssl
Requires:       php-pcre
Requires:       php-pdo
Requires:       php-session
Requires:       php-simplexml
Requires:       php-xmlwriter
Requires:       php-spl
Requires:       php-zip
Requires:       php-filter
Requires:       php-ldap
Requires:       php-smbclient
Requires:       php-gmp
Requires:       php-process
Requires:       php-pecl-imagick
Requires:       php-pecl-memcached
Requires:       php-pecl-apcu
Requires:       php-pecl-redis5
# For systemd support during install/uninstall
%{?systemd_requires}
# the CA cert bundle is linked to from the config dir
Requires:       %{_sysconfdir}/pki/tls/certs/ca-bundle.crt

# Bundled composer libraries
# many of these can be unbundled
Provides: bundled(php-composer(aws/aws-sdk-php)) = 3.171.21
Provides: bundled(php-composer(bantu/ini-get-wrapper)) = 1.0.1
Provides: bundled(php-composer(beberlei/assert)) = 3.3.0
Provides: bundled(php-composer(brick/math)) = 0.9.1
Provides: bundled(php-composer(christophwurst/id3parser)) = 0.1.4
Provides: bundled(php-composer(cweagans/composer-patches)) = 1.7
Provides: bundled(php-composer(deepdiver/zipstreamer)) = 2.0.0
Provides: bundled(php-composer(deepdiver1975/tarstreamer)) = 2.0.0
Provides: bundled(php-composer(doctrine/cache)) = 1.10.2
Provides: bundled(php-composer(doctrine/dbal)) = 3.1.4
Provides: bundled(php-composer(doctrine/event-manager)) = 1.1.1
Provides: bundled(php-composer(doctrine/lexer)) = 1.2.1
Provides: bundled(php-composer(egulias/email-validator)) = 3.1.1
Provides: bundled(php-composer(fgrosse/phpasn1)) = 2.2.0
Provides: bundled(php-composer(giggsey/libphonenumber-for-php)) = 8.12.37
Provides: bundled(php-composer(giggsey/locale)) = 1.9
Provides: bundled(php-composer(guzzlehttp/guzzle)) = 7.4.0
Provides: bundled(php-composer(guzzlehttp/promises)) = 1.4.0
Provides: bundled(php-composer(guzzlehttp/psr7)) = 1.7.0
Provides: bundled(php-composer(guzzlehttp/uri-template)) = 0.2.0
Provides: bundled(php-composer(icewind/searchdav)) = 3.0
Provides: bundled(php-composer(icewind/smb)) = 3.2.7
Provides: bundled(php-composer(icewind/streams)) = 0.7.5
Provides: bundled(php-composer(justinrainbow/json-schema)) = 5.2.10
Provides: bundled(php-composer(league/uri)) = 6.4.0
Provides: bundled(php-composer(league/uri-interfaces)) = 2.2.0
Provides: bundled(php-composer(microsoft/azure-storage-blob)) = 1.5.2
Provides: bundled(php-composer(microsoft/azure-storage-common)) = 1.5.1
Provides: bundled(php-composer(mtdowling/jmespath.php)) = 2.6.0
Provides: bundled(php-composer(nextcloud/lognormalizer)) = 1.0.0
Provides: bundled(php-composer(nikic/php-parser)) = 4.10.4
Provides: bundled(php-composer(opis/closure)) = 3.6.1
Provides: bundled(php-composer(pear/archive_tar)) = 1.4.12
Provides: bundled(php-composer(pear/console_getopt)) = 1.4.3
Provides: bundled(php-composer(pear/pear-core-minimal)) = 1.10.10
Provides: bundled(php-composer(pear/pear_exception)) = 1.0.1
Provides: bundled(php-composer(php-ds/php-ds)) = 1.3.0
Provides: bundled(php-composer(php-http/guzzle7-adapter)) = 1.0.0
Provides: bundled(php-composer(php-http/httplug)) = 2.2.0
Provides: bundled(php-composer(php-http/promise)) = 1.1.0
Provides: bundled(php-composer(php-opencloud/openstack)) = 3.1.0
Provides: bundled(php-composer(phpseclib/phpseclib)) = 2.0.32
Provides: bundled(php-composer(pimple/pimple)) = 3.5.0
Provides: bundled(php-composer(psr/container)) = 1.1.1
Provides: bundled(php-composer(psr/event-dispatcher)) = 1.0
Provides: bundled(php-composer(psr/http-client)) = 1.0.1
Provides: bundled(php-composer(psr/http-factory)) = 1.0.1
Provides: bundled(php-composer(psr/http-message)) = 1.0.1
Provides: bundled(php-composer(psr/log)) = 1.1.3
Provides: bundled(php-composer(punic/punic)) = 1.6.5
Provides: bundled(php-composer(ralouphie/getallheaders)) = 3.0.3
Provides: bundled(php-composer(ramsey/collection)) = 1.1.1
Provides: bundled(php-composer(ramsey/uuid)) = 4.1.1
Provides: bundled(php-composer(sabre/dav)) = 4.2.1
Provides: bundled(php-composer(sabre/event)) = 5.1.2
Provides: bundled(php-composer(sabre/http)) = 5.1.1
Provides: bundled(php-composer(sabre/uri)) = 2.2.1
Provides: bundled(php-composer(sabre/vobject)) = 4.3.3
Provides: bundled(php-composer(sabre/xml)) = 2.2.3
Provides: bundled(php-composer(scssphp/scssphp)) = 1.8.1
Provides: bundled(php-composer(spomky-labs/base64url)) = 2.0.4
Provides: bundled(php-composer(spomky-labs/cbor-php)) = 2.0.1
Provides: bundled(php-composer(stecman/symfony-console-completion)) = 0.11.0
Provides: bundled(php-composer(swiftmailer/swiftmailer)) = 6.2.5
Provides: bundled(php-composer(symfony/console)) = 4.4.30
Provides: bundled(php-composer(symfony/event-dispatcher)) = 4.4.30
Provides: bundled(php-composer(symfony/event-dispatcher-contracts)) = 1.1.9
Provides: bundled(php-composer(symfony/polyfill-ctype)) = 1.22.0
Provides: bundled(php-composer(symfony/polyfill-iconv)) = 1.22.0
Provides: bundled(php-composer(symfony/polyfill-intl-grapheme)) = 1.22.0
Provides: bundled(php-composer(symfony/polyfill-intl-idn)) = 1.22.0
Provides: bundled(php-composer(symfony/polyfill-intl-normalizer)) = 1.22.0
Provides: bundled(php-composer(symfony/polyfill-mbstring)) = 1.22.0
Provides: bundled(php-composer(symfony/polyfill-php72)) = 1.22.0
Provides: bundled(php-composer(symfony/polyfill-php73)) = 1.22.0
Provides: bundled(php-composer(symfony/polyfill-php80)) = 1.22.0
Provides: bundled(php-composer(symfony/process)) = 4.4.30
Provides: bundled(php-composer(symfony/routing)) = 4.4.30
Provides: bundled(php-composer(symfony/service-contracts)) = 2.2.0
Provides: bundled(php-composer(symfony/translation)) = 4.4.41
Provides: bundled(php-composer(symfony/translation-contracts)) = 2.3.0
Provides: bundled(php-composer(thecodingmachine/safe)) = 1.3.3
Provides: bundled(php-composer(web-auth/cose-lib)) = 3.3.1
Provides: bundled(php-composer(web-auth/metadata-service)) = 3.3.1
Provides: bundled(php-composer(web-auth/webauthn-lib)) = 3.3.1

# OpenIconic icons bundled via sabre-dav
Provides:       bundled(openiconic-fonts) = 1.0.0
# jscolor bundled via themeing app
Provides:       bundled(jscolor) = 2.0.4
# jquery-ui-multiselect bundled via user_ldap app
Provides:       bundled(jquery-ui-multiselect) = 1.13
# zxcvbn bundled via core
Provides:       bundled(zxcvbn) = 4.4.2

%description
NextCloud gives you universal access to your files through a web interface or
WebDAV. It also provides a platform to easily view & sync your contacts,
calendars and bookmarks across all your devices and enables basic editing right
on the web. NextCloud is extendable via a simple but powerful API for
applications and plugins.


%package httpd
Summary:        Httpd integration for NextCloud
Provides:       %{name}-webserver = %{version}-%{release}
Requires:       %{name} = %{version}-%{release}
# PHP dependencies
Requires:       php-fpm httpd

%description httpd
%{summary}.


%package nginx
Summary:        Nginx integration for NextCloud
Provides:       %{name}-webserver = %{version}-%{release}
Requires:       %{name} = %{version}-%{release}
# PHP dependencies
Requires:       php-fpm nginx

%description nginx
%{summary}.


%package mysql
Summary:        MySQL database support for NextCloud
Provides:       %{name}-database = %{version}-%{release}
Requires:       %{name} = %{version}-%{release}
# From getSupportedDatabases, mysql => pdo, mysql
Requires:       php-mysqlnd

%description mysql
This package ensures the necessary dependencies are in place for NextCloud to
work with MySQL / MariaDB databases. It does not require a MySQL / MariaDB
server to be installed, as you may well wish to use a remote database
server.

If you want the database to be on the same system as NextCloud itself, you must
also install and enable a MySQL / MariaDB server package. See README.mysql for
more details.

%package postgresql
Summary:        PostgreSQL database support for NextCloud
Provides:       %{name}-database = %{version}-%{release}
Requires:       %{name} = %{version}-%{release}
# From getSupportedDatabases, pgsql => function, pg_connect
Requires:       php-pgsql

%description postgresql
This package ensures the necessary dependencies are in place for NextCloud to
work with a PostgreSQL database. It does not require the PostgreSQL server
package to be installed, as you may well wish to use a remote database
server.

If you want the database to be on the same system as NextCloud itself, you must
also install and enable the PostgreSQL server package. See README.postgresql
for more details.


%package sqlite
Summary:        SQLite 3 database support for NextCloud
Provides:       %{name}-database = %{version}-%{release}
Requires:       %{name} = %{version}-%{release}
# From getSupportedDatabases, pgsql => class, SQLite3

%description sqlite
This package ensures the necessary dependencies are in place for NextCloud to
work with an SQLite 3 database stored on the local system.


%prep
%autosetup -n %{name} -p1

# patch backup files and .git stuff
find . -name \*.orig    -type f        -exec rm    {} \; -print
find . -name .gitignore -type f        -exec rm    {} \; -print
find . -name .github    -type d -prune -exec rm -r {} \; -print

# prepare package doc
cp %{SOURCE300} README.fedora
cp %{SOURCE301} README.mysql
cp %{SOURCE302} README.postgresql
cp %{SOURCE303} MIGRATION.fedora

# Locate license files and put them sensibly in place
# get rid of all composer licenses
find -wholename "*/composer/LICENSE" -exec mv {} composer-LICENSE \;

# find all remaining using "find -name '*LICENCE*' -name '*LICENSE*' -o -name '*COPYING*' | sort"
mv dist/*LICENSE.txt .
mv 3rdparty/aws/aws-sdk-php/LICENSE.md aws-LICENSE.md
mv 3rdparty/bantu/ini-get-wrapper/LICENSE bantu-LICENSE
mv 3rdparty/beberlei/assert/LICENSE beberlei-LICENSE
mv 3rdparty/brick/math/LICENSE brick-LICENSE
mv 3rdparty/christophwurst/id3parser/LICENSE christophwurst-LICENSE
mv 3rdparty/composer/package-versions-deprecated/LICENSE composer-LICENSE
mv 3rdparty/cweagans/composer-patches/LICENSE.md cweagans-LICENSE
mv 3rdparty/deepdiver1975/tarstreamer/LICENSE deepdiver1975-LICENSE
mv 3rdparty/deepdiver/zipstreamer/COPYING deepdiver-COPYING
mv 3rdparty/doctrine/cache/LICENSE doctrine-LICENSE
mv 3rdparty/doctrine/dbal/LICENSE doctrine-LICENSE
mv 3rdparty/doctrine/event-manager/LICENSE doctrine-LICENSE
mv 3rdparty/egulias/email-validator/LICENSE egulias-LICENSE
mv 3rdparty/fgrosse/phpasn1/LICENSE fgrosse-LICENSE
mv 3rdparty/giggsey/libphonenumber-for-php/LICENSE giggsey-LICENSE
mv 3rdparty/giggsey/locale/LICENSE giggsey-LICENSE
mv 3rdparty/guzzlehttp/guzzle/LICENSE guzzlehttp-LICENSE
mv 3rdparty/guzzlehttp/promises/LICENSE guzzlehttp-LICENSE
mv 3rdparty/guzzlehttp/psr7/LICENSE guzzlehttp-LICENSE
mv 3rdparty/guzzlehttp/uri-template/LICENSE.md guzzlehttp-LICENSE
mv 3rdparty/icewind/searchdav/LICENSE icewind-LICENSE
mv 3rdparty/justinrainbow/json-schema/LICENSE justinrainbow-LICENSE
mv 3rdparty/league/uri-interfaces/LICENSE league-LICENSE
mv 3rdparty/league/uri/LICENSE league-LICENSE
mv '3rdparty/LICENSE INFO' 3rdparty-LICENSE_INFO
mv 3rdparty/microsoft/azure-storage-blob/LICENSE microsoft-LICENSE
mv 3rdparty/microsoft/azure-storage-common/LICENSE microsoft-LICENSE
mv 3rdparty/mtdowling/jmespath.php/LICENSE mtdowling-LICENSE
mv 3rdparty/nextcloud/lognormalizer/COPYING lognormalizer-LICENSE
mv 3rdparty/nikic/php-parser/LICENSE nikic-LICENSE
mv 3rdparty/opis/closure/LICENSE opis-LICENSE
mv 3rdparty/pear/console_getopt/LICENSE pear-LICENSE
mv 3rdparty/pear/pear_exception/LICENSE pear-LICENSE
mv 3rdparty/php-ds/php-ds/LICENSE php-ds-LICENSE
mv 3rdparty/php-http/guzzle7-adapter/LICENSE php-http-LICENSE
mv 3rdparty/php-http/httplug/LICENSE php-http-LICENSE
mv 3rdparty/php-http/promise/LICENSE php-http-LICENSE
mv 3rdparty/php-opencloud/openstack/LICENSE php-opencloud-LICENSE
mv 3rdparty/phpseclib/phpseclib/LICENSE phpseclib-LICENSE
mv 3rdparty/psr/event-dispatcher/LICENSE psr-LICENSE
mv 3rdparty/psr/container/LICENSE psr-LICENSE
mv 3rdparty/psr/http-client/LICENSE psr-LICENSE
mv 3rdparty/psr/http-factory/LICENSE psr-LICENSE
mv 3rdparty/psr/http-message/LICENSE psr-LICENSE
mv 3rdparty/psr/log/LICENSE psr-LICENSE
mv 3rdparty/punic/punic/LICENSE.txt punic-LICENSE.txt
mv 3rdparty/punic/punic/UNICODE-LICENSE.txt punic-UNICODE-LICENSE
mv 3rdparty/ralouphie/getallheaders/LICENSE ralouphie-LICENSE
mv 3rdparty/ramsey/collection/LICENSE ramsey-LICENSE
mv 3rdparty/ramsey/uuid/LICENSE ramsey-LICENSE
mv 3rdparty/sabre/dav/lib/DAV/Browser/assets/openiconic/ICON-LICENSE sabre-ICON-LICENSE
mv 3rdparty/sabre/dav/LICENSE sabre-LICENSE
mv 3rdparty/sabre/event/LICENSE sabre-LICENSE
mv 3rdparty/sabre/http/LICENSE sabre-LICENSE
mv 3rdparty/sabre/uri/LICENSE sabre-LICENSE
mv 3rdparty/sabre/vobject/LICENSE sabre-LICENSE
mv 3rdparty/sabre/xml/LICENSE sabre-LICENSE
mv 3rdparty/scssphp/scssphp/LICENSE.md scssphp-LICENSE.md
mv 3rdparty/spomky-labs/base64url/LICENSE spomky-labs-LICENSE
mv 3rdparty/spomky-labs/cbor-php/LICENSE spomky-labs-LICENSE
mv 3rdparty/stecman/symfony-console-completion/LICENCE stecman-LICENSE
mv 3rdparty/symfony/console/LICENSE symfony-LICENSE
mv 3rdparty/symfony/deprecation-contracts/LICENSE symfony-LICENSE
mv 3rdparty/symfony/event-dispatcher-contracts/LICENSE symfony-LICENSE
mv 3rdparty/symfony/event-dispatcher/LICENSE symfony-LICENSE
mv 3rdparty/symfony/polyfill-ctype/LICENSE symfony-LICENSE
mv 3rdparty/symfony/polyfill-iconv/LICENSE symfony-LICENSE
mv 3rdparty/symfony/polyfill-intl-grapheme/LICENSE symfony-LICENSE
mv 3rdparty/symfony/polyfill-intl-idn/LICENSE symfony-LICENSE
mv 3rdparty/symfony/polyfill-intl-normalizer/LICENSE symfony-LICENSE
mv 3rdparty/symfony/polyfill-mbstring/LICENSE symfony-LICENSE
mv 3rdparty/symfony/polyfill-php72/LICENSE symfony-LICENSE
mv 3rdparty/symfony/polyfill-php73/LICENSE symfony-LICENSE
mv 3rdparty/symfony/polyfill-php80/LICENSE symfony-LICENSE
mv 3rdparty/symfony/process/LICENSE symfony-LICENSE
mv 3rdparty/symfony/routing/LICENSE symfony-LICENSE
mv 3rdparty/symfony/service-contracts/LICENSE symfony-LICENSE
mv 3rdparty/symfony/translation-contracts/LICENSE symfony-LICENSE
mv 3rdparty/symfony/translation/LICENSE symfony-LICENSE
mv 3rdparty/thecodingmachine/safe/LICENSE thecodingmachine-LICENSE
mv 3rdparty/web-auth/cose-lib/LICENSE web-auth-LICENSE
mv 3rdparty/web-auth/metadata-service/LICENSE web-auth-LICENSE
mv 3rdparty/web-auth/webauthn-lib/LICENSE web-auth-LICENSE
mv apps/activity/js/activity-sidebar.js.LICENSE.txt activity-sidebar.js-LICENSE
mv apps/activity/js/activity-dashboard.js.LICENSE.txt activity-dashboard.js-LICENSE
mv apps/circles/LICENSE circles-LICENSE
mv apps/cloud_federation_api/LICENSE cloud_federation_api-LICENSE
mv apps/files_external/3rdparty/icewind/smb/LICENSE.txt icewind-LICENSE
mv apps/files_external/3rdparty/icewind/streams/LICENCE icewind-LICENSE
mv apps/files_pdfviewer/COPYING files_pdfviewer-COPYING
mv apps/files_pdfviewer/js/files_pdfviewer-workersrc.js.LICENSE.txt files_pdfviewer-workersrc.js-LICENSE
mv apps/files_pdfviewer/js/files_pdfviewer-main.js.LICENSE.txt files_pdfviewer-main.js-LICENSE
mv apps/files_pdfviewer/js/files_pdfviewer-public.js.LICENSE.txt files_pdfviewer-public.js-LICENSE
mv apps/files_pdfviewer/js/pdfjs/LICENSE js-pdfjs-LICENSE
mv apps/files_pdfviewer/js/pdfjs/web/cmaps/LICENSE js-pdfjs-cmaps-LICENSE
mv apps/files_pdfviewer/js/pdfjs/web/standard_fonts/LICENSE_LIBERATION js-pdfjs-LICENSE_LIBERATION
mv apps/files_pdfviewer/js/pdfjs/web/standard_fonts/LICENSE_FOXIT js-pdfjs-LICENSE_FOXIT
mv apps/files_rightclick/COPYING files_rightclick-COPYING
mv apps/files_rightclick/LICENSE files_rightclick-LICENSE
mv apps/files_videoplayer/js/files_videoplayer-main.js.LICENSE.txt files_videoplayer-main.js-LICENSE
mv apps/files_videoplayer/js/files_videoplayer-vendors-node_modules_video_js_dist_video_es_js.js.LICENSE.txt files_videoplayer-node_modules_video_js_dist_video_es_js.js-LICENSE
mv apps/firstrunwizard/js/firstrunwizard-main.js.LICENSE.txt firstrunwizard-LICENSE
mv apps/logreader/js/logreader-main.js.LICENSE.txt logreader-main.js-LICENSE
mv apps/nextcloud_announcements/COPYING nextcloud_announcements-COPYING
mv apps/notifications/COPYING notifications-LICENSE
mv apps/notifications/js/notifications-main.js.LICENSE.txt notifications-main.js-LICENSE
mv apps/notifications/js/notifications-settings.js.LICENSE.txt notifications-main.js-LICENSE
mv apps/password_policy/LICENSE password_policy-LICENSE
mv apps/password_policy/js/password_policy-settings.js.LICENSE.txt password_policy-settings.js-LICENSE
mv apps/photos/COPYING photos-COPYING
mv apps/photos/js/photos-main.js.LICENSE.txt photos-main.js-LICENSE
mv apps/photos/js/photos-node_modules_nextcloud_moment_node_modules_moment_locale_sync_recursive_-src_patchedRequest_j-3cb869.js.LICENSE.txt photos-node_modules_nextcloud_moment_node_modules_moment_locale_sync_recursive_-LICENSE
mv apps/photos/js/photos-vendors-node_modules_nextcloud_moment_dist_index_js-node_modules_nextcloud_moment_node_module-ca085a.js.LICENSE.txt photos-vendors1.js-LICENSE
mv apps/photos/js/photos-vendors-node_modules_nextcloud_moment_dist_index_js-node_modules_moment_locale_af_js-node_mod-100548.js.LICENSE.txt photos-vendors2.js-LICENSE
mv apps/photos/js/photos-src_views_Albums_vue.js.LICENSE.txt photos-src_views_Albums_vue.js-LICENSE
mv apps/photos/js/photos-src_patchedRequest_js-src_views_Tags_vue.js.LICENSE.txt photos-src_patchedRequest_js.js-LICENSE
mv apps/photos/js/photos-vendors-node_modules_nextcloud_vue_dist_Components_ActionButton_js-node_modules_nextcloud_vue-208129.js.LICENSE.txt photos-vendors3.js-LICENSE
mv apps/photos/js/photos-src_patchedRequest_js-node_modules_moment_locale_sync_recursive_-src_views_Timeline_vue.js.LICENSE.txt photos-src_patchedRequest_js.js-LICENSE
mv apps/photos/js/photos-src_mixins_GridConfig_js-src_utils_CancelableRequest_js-src_components_EmptyContent_vue-src_c-45f6cf.js.LICENSE.txt photos-src_mixins_GridConfig_js.js-LICENSE
mv apps/photos/js/photos-vendors-node_modules_webdav_dist_node_index_js-node_modules_webdav_dist_node_request_js.js.LICENSE.txt photos-vendors4.js-LICENSE
mv apps/privacy/COPYING privacy-COPYING
mv apps/privacy/js/privacy-main.js.LICENSE.txt privacy-main.js-LICENSE
mv apps/recommendations/LICENSE recommendations-LICENSE
mv apps/serverinfo/COPYING serverinfo-LICENSE
mv apps/survey_client/COPYING survey_client-LICENSE
mv apps/text/COPYING text-COPYING
mv apps/text/js/*.js.LICENSE.txt .
mv apps/theming/js/3rdparty/jscolor/LICENSE.txt jscolor-LICENSE
mv apps/user_ldap/js/vendor/ui-multiselect/MIT-LICENSE js-jqueryui-multiselect-LICENSE
mv apps/viewer/COPYING viewer-COPYING
mv apps/viewer/js/viewer-main.js.LICENSE.txt viewer-main.js-LICENSE
mv COPYING nextcloud-LICENSE
mv core/fonts/LICENSE_OFL.txt fonts-LICENSE
mv core/vendor/zxcvbn/LICENSE.txt zxcvbn-LICENSE

%check
# Make sure there are no license files left over
: Check for leftover license files
find . -mindepth 2 \( -name '*LICENSE*' -o -name '*LICENCE*' -o  -name '*COPYING*' \)
nb=$( find . -mindepth 2 \( -name '*LICENSE*' -o -name '*LICENCE*' -o  -name '*COPYING*' \) | wc -l )
if [ $nb -gt 0 ]
  then
  false Found unexpected licenses to verify
fi


%build
# Nothing to build

%install
install -dm 755 %{buildroot}%{_datadir}/%{name}

# create nextcloud datadir
mkdir -p %{buildroot}%{_localstatedir}/lib/%{name}/data
# create writable app dir for appstore
mkdir -p %{buildroot}%{_localstatedir}/lib/%{name}/apps
# create nextcloud sysconfdir
mkdir -p %{buildroot}%{_sysconfdir}/%{name}

# install content
for d in $(find . -mindepth 1 -maxdepth 1 -type d | grep -v config); do
    cp -a "$d" %{buildroot}%{_datadir}/%{name}
done

for f in {*.php,*.html,robots.txt}; do
    install -pm 644 "$f" %{buildroot}%{_datadir}/%{name}
done

# occ should be executable
install -pm 755 occ %{buildroot}%{_datadir}/%{name}

# symlink config dir
ln -sf %{_sysconfdir}/%{name} %{buildroot}%{_datadir}/%{name}/config

# nextcloud looks for ca-bundle.crt in config dir
ln -sf %{_sysconfdir}/pki/tls/certs/ca-bundle.crt %{buildroot}%{_sysconfdir}/%{name}/ca-bundle.crt

# set default config
install -pm 644 %{SOURCE1}    %{buildroot}%{_sysconfdir}/%{name}/config.php

# httpd config
install -Dpm 644 %{SOURCE100} \
    %{buildroot}%{_sysconfdir}/httpd/conf.d/%{name}.conf
install -Dpm 644 %{SOURCE101} \
    %{buildroot}%{_sysconfdir}/httpd/conf.d/%{name}-access.conf.avail
install -Dpm 644 %{SOURCE102} %{SOURCE103} %{SOURCE104} %{SOURCE105} \
    %{buildroot}%{_sysconfdir}/httpd/conf.d/

# nginx config
install -Dpm 644 %{SOURCE200} \
    %{buildroot}%{_sysconfdir}/nginx/default.d/%{name}.conf
install -Dpm 644 %{SOURCE201} \
    %{buildroot}%{_sysconfdir}/nginx/conf.d/%{name}.conf

# php-fpm config
install -Dpm 644 %{SOURCE202} \
    %{buildroot}%{_sysconfdir}/php-fpm.d/%{name}.conf

# Install the systemd timer
install -Dpm 644 %{SOURCE2} %{buildroot}%{_unitdir}/nextcloud-cron.service
install -Dpm 644 %{SOURCE3} %{buildroot}%{_unitdir}/nextcloud-cron.timer

%post httpd
/usr/bin/systemctl reload httpd.service > /dev/null 2>&1 || :
/usr/bin/systemctl reload php-fpm.service > /dev/null 2>&1 || :

%postun httpd
if [ $1 -eq 0 ]; then
  /usr/bin/systemctl reload httpd.service > /dev/null 2>&1 || :
  /usr/bin/systemctl reload php-fpm.service > /dev/null 2>&1 || :
fi

%post nginx
/usr/bin/systemctl reload nginx.service > /dev/null 2>&1 || :
/usr/bin/systemctl reload php-fpm.service > /dev/null 2>&1 || :

%postun nginx
if [ $1 -eq 0 ]; then
  /usr/bin/systemctl reload nginx.service > /dev/null 2>&1 || :
  /usr/bin/systemctl reload php-fpm.service > /dev/null 2>&1 || :
fi

%files
%doc AUTHORS README.fedora MIGRATION.fedora config/config.sample.php
%license *-LICENSE
%dir %attr(-,apache,apache) %{_sysconfdir}/%{name}
# contains sensitive data (dbpassword, passwordsalt)
%config(noreplace) %attr(0600,apache,apache) %{_sysconfdir}/%{name}/config.php
# need the symlink in confdir but it's not config
%{_sysconfdir}/%{name}/ca-bundle.crt
%{_datadir}/%{name}
%dir %attr(0755,apache,apache) %{_localstatedir}/lib/%{name}
# user data must not be world readable
%dir %attr(0750,apache,apache) %{_localstatedir}/lib/%{name}/data
%attr(-,apache,apache) %{_localstatedir}/lib/%{name}/apps
%{_unitdir}/nextcloud-cron.service
%{_unitdir}/nextcloud-cron.timer

%files httpd
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf
%{_sysconfdir}/httpd/conf.d/%{name}-access.conf.avail
%{_sysconfdir}/httpd/conf.d/%{name}*.inc
%config(noreplace) %{_sysconfdir}/php-fpm.d/%{name}.conf

%files nginx
%config(noreplace) %{_sysconfdir}/nginx/default.d/%{name}.conf
%config(noreplace) %{_sysconfdir}/nginx/conf.d/%{name}.conf
%config(noreplace) %{_sysconfdir}/php-fpm.d/%{name}.conf

%files mysql
%doc README.mysql
%files postgresql
%doc README.postgresql
%files sqlite
