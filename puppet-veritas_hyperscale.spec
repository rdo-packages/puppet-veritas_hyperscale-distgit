%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:                   puppet-veritas_hyperscale
Version:                XXX
Release:                XXX
Summary:                Veritas HyperScale installer.
License:                Apache 2.0

URL:                    https://github.com/vtas-hyperscale-ci/puppet-veritas_hyperscale

Source0:                https://github.com/vtas-hyperscale-ci/puppet-veritas_hyperscale/archive/%{version}.tar.gz

BuildArch:              noarch

Requires:               puppet-stdlib
Requires:               puppet-anyjson
Requires:               puppet-amqp
Requires:               puppet-kombu
Requires:               puppet-kazoo
Requires:               puppet-sqlalchemy
Requires:               lvm2
Requires:               crudini
Requires:               coreutils

Requires:               puppet >= 2.7.0

%description -n puppet-veritas_hyperscale
puppet-veritas_hyperscale is a module that installs Veritas Hyperscale.

%prep
%setup -q -n %{name}-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/veritas_hyperscale/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/veritas_hyperscale/



%files
%{_datadir}/openstack-puppet/modules/veritas_hyperscale/


%changelog
