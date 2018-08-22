%{!?upstream_version: %global upstream_version %{commit}}
%global commit 7c7868adb027c5bcfdcb6fc9d86610470759ae28
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git

Name:                   puppet-veritas_hyperscale
Version:                1.0.0
Release:                1%{?alphatag}%{?dist}
Summary:                Veritas HyperScale installer.
License:                ASL 2.0

URL:                    https://github.com/vtas-hyperscale-ci/puppet-veritas_hyperscale

Source0:                https://github.com/vtas-hyperscale-ci/puppet-veritas_hyperscale/archive/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz

BuildArch:              noarch

Requires:               puppet-stdlib
Requires:               puppet-rabbitmq
Requires:               puppet-keystone
Requires:               puppet-nova
Requires:               puppet-cinder
Requires:               puppet-openstacklib

Requires:               puppet >= 2.7.0

%description
Installs and configures Veritas Hyperscale (Controller).

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
* Thu Feb 15 2018 RDO <dev@lists.rdoproject.org> 1.0.0-1.7c7868agit
- Update to post 1.0.0 (7c7868adb027c5bcfdcb6fc9d86610470759ae28)

