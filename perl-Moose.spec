#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v3
# autospec commit: 1eaf8cd
#
Name     : perl-Moose
Version  : 2.2207
Release  : 34
URL      : https://cpan.metacpan.org/authors/id/E/ET/ETHER/Moose-2.2207.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/ET/ETHER/Moose-2.2207.tar.gz
Summary  : 'A postmodern object system for Perl 5'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Moose-bin = %{version}-%{release}
Requires: perl-Moose-license = %{version}-%{release}
Requires: perl-Moose-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(CPAN::Meta::Check)
BuildRequires : perl(Class::Load)
BuildRequires : perl(Class::Load::XS)
BuildRequires : perl(Data::OptList)
BuildRequires : perl(Devel::GlobalDestruction)
BuildRequires : perl(Devel::OverloadInfo)
BuildRequires : perl(Devel::StackTrace)
BuildRequires : perl(Dist::CheckConflicts)
BuildRequires : perl(Eval::Closure)
BuildRequires : perl(MRO::Compat)
BuildRequires : perl(Module::Runtime)
BuildRequires : perl(Module::Runtime::Conflicts)
BuildRequires : perl(Package::DeprecationManager)
BuildRequires : perl(Package::Stash)
BuildRequires : perl(Package::Stash::XS)
BuildRequires : perl(Params::Util)
BuildRequires : perl(Sub::Exporter)
BuildRequires : perl(Test::Fatal)
BuildRequires : perl(Test::Needs)
BuildRequires : perl(Try::Tiny)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
[![CPAN version](https://badge.fury.io/pl/Moose.svg)](http://badge.fury.io/pl/Moose)
[![Build Status](https://travis-ci.org/moose/Moose.png?branch=master,stable/2.12)](https://travis-ci.org/moose/Moose)
[![Coverage Status](https://coveralls.io/repos/moose/Moose/badge.png?branch=master)](https://coveralls.io/r/moose/Moose?branch=master)

%package bin
Summary: bin components for the perl-Moose package.
Group: Binaries
Requires: perl-Moose-license = %{version}-%{release}

%description bin
bin components for the perl-Moose package.


%package dev
Summary: dev components for the perl-Moose package.
Group: Development
Requires: perl-Moose-bin = %{version}-%{release}
Provides: perl-Moose-devel = %{version}-%{release}
Requires: perl-Moose = %{version}-%{release}

%description dev
dev components for the perl-Moose package.


%package license
Summary: license components for the perl-Moose package.
Group: Default

%description license
license components for the perl-Moose package.


%package perl
Summary: perl components for the perl-Moose package.
Group: Default
Requires: perl-Moose = %{version}-%{release}

%description perl
perl components for the perl-Moose package.


%prep
%setup -q -n Moose-2.2207
cd %{_builddir}/Moose-2.2207
pushd ..
cp -a Moose-2.2207 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Moose
cp %{_builddir}/Moose-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Moose/c173a21aa3da707ecef101c038841171903a78d2 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/moose-outdated

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Class::MOP.3
/usr/share/man/man3/Class::MOP::Attribute.3
/usr/share/man/man3/Class::MOP::Class.3
/usr/share/man/man3/Class::MOP::Class::Immutable::Trait.3
/usr/share/man/man3/Class::MOP::Deprecated.3
/usr/share/man/man3/Class::MOP::Instance.3
/usr/share/man/man3/Class::MOP::Method.3
/usr/share/man/man3/Class::MOP::Method::Accessor.3
/usr/share/man/man3/Class::MOP::Method::Constructor.3
/usr/share/man/man3/Class::MOP::Method::Generated.3
/usr/share/man/man3/Class::MOP::Method::Inlined.3
/usr/share/man/man3/Class::MOP::Method::Meta.3
/usr/share/man/man3/Class::MOP::Method::Wrapped.3
/usr/share/man/man3/Class::MOP::MiniTrait.3
/usr/share/man/man3/Class::MOP::Mixin.3
/usr/share/man/man3/Class::MOP::Mixin::AttributeCore.3
/usr/share/man/man3/Class::MOP::Mixin::HasAttributes.3
/usr/share/man/man3/Class::MOP::Mixin::HasMethods.3
/usr/share/man/man3/Class::MOP::Mixin::HasOverloads.3
/usr/share/man/man3/Class::MOP::Module.3
/usr/share/man/man3/Class::MOP::Object.3
/usr/share/man/man3/Class::MOP::Overload.3
/usr/share/man/man3/Class::MOP::Package.3
/usr/share/man/man3/Moose.3
/usr/share/man/man3/Moose::Conflicts.3
/usr/share/man/man3/Moose::Cookbook.3
/usr/share/man/man3/Moose::Cookbook::Basics::BankAccount_MethodModifiersAndSubclassing.3
/usr/share/man/man3/Moose::Cookbook::Basics::BinaryTree_AttributeFeatures.3
/usr/share/man/man3/Moose::Cookbook::Basics::BinaryTree_BuilderAndLazyBuild.3
/usr/share/man/man3/Moose::Cookbook::Basics::Company_Subtypes.3
/usr/share/man/man3/Moose::Cookbook::Basics::DateTime_ExtendingNonMooseParent.3
/usr/share/man/man3/Moose::Cookbook::Basics::Document_AugmentAndInner.3
/usr/share/man/man3/Moose::Cookbook::Basics::Genome_OverloadingSubtypesAndCoercion.3
/usr/share/man/man3/Moose::Cookbook::Basics::HTTP_SubtypesAndCoercion.3
/usr/share/man/man3/Moose::Cookbook::Basics::Immutable.3
/usr/share/man/man3/Moose::Cookbook::Basics::Person_BUILDARGSAndBUILD.3
/usr/share/man/man3/Moose::Cookbook::Basics::Point_AttributesAndSubclassing.3
/usr/share/man/man3/Moose::Cookbook::Extending::Debugging_BaseClassRole.3
/usr/share/man/man3/Moose::Cookbook::Extending::ExtensionOverview.3
/usr/share/man/man3/Moose::Cookbook::Extending::Mooseish_MooseSugar.3
/usr/share/man/man3/Moose::Cookbook::Legacy::Debugging_BaseClassReplacement.3
/usr/share/man/man3/Moose::Cookbook::Legacy::Labeled_AttributeMetaclass.3
/usr/share/man/man3/Moose::Cookbook::Legacy::Table_ClassMetaclass.3
/usr/share/man/man3/Moose::Cookbook::Meta::GlobRef_InstanceMetaclass.3
/usr/share/man/man3/Moose::Cookbook::Meta::Labeled_AttributeTrait.3
/usr/share/man/man3/Moose::Cookbook::Meta::PrivateOrPublic_MethodMetaclass.3
/usr/share/man/man3/Moose::Cookbook::Meta::Table_MetaclassTrait.3
/usr/share/man/man3/Moose::Cookbook::Meta::WhyMeta.3
/usr/share/man/man3/Moose::Cookbook::Roles::ApplicationToInstance.3
/usr/share/man/man3/Moose::Cookbook::Roles::Comparable_CodeReuse.3
/usr/share/man/man3/Moose::Cookbook::Roles::Restartable_AdvancedComposition.3
/usr/share/man/man3/Moose::Cookbook::Snack::Keywords.3
/usr/share/man/man3/Moose::Cookbook::Snack::Types.3
/usr/share/man/man3/Moose::Cookbook::Style.3
/usr/share/man/man3/Moose::Deprecated.3
/usr/share/man/man3/Moose::Exception.3
/usr/share/man/man3/Moose::Exporter.3
/usr/share/man/man3/Moose::Intro.3
/usr/share/man/man3/Moose::Manual.3
/usr/share/man/man3/Moose::Manual::Attributes.3
/usr/share/man/man3/Moose::Manual::BestPractices.3
/usr/share/man/man3/Moose::Manual::Classes.3
/usr/share/man/man3/Moose::Manual::Concepts.3
/usr/share/man/man3/Moose::Manual::Construction.3
/usr/share/man/man3/Moose::Manual::Contributing.3
/usr/share/man/man3/Moose::Manual::Delegation.3
/usr/share/man/man3/Moose::Manual::Delta.3
/usr/share/man/man3/Moose::Manual::Exceptions.3
/usr/share/man/man3/Moose::Manual::Exceptions::Manifest.3
/usr/share/man/man3/Moose::Manual::FAQ.3
/usr/share/man/man3/Moose::Manual::MOP.3
/usr/share/man/man3/Moose::Manual::MethodModifiers.3
/usr/share/man/man3/Moose::Manual::MooseX.3
/usr/share/man/man3/Moose::Manual::Resources.3
/usr/share/man/man3/Moose::Manual::Roles.3
/usr/share/man/man3/Moose::Manual::Support.3
/usr/share/man/man3/Moose::Manual::Types.3
/usr/share/man/man3/Moose::Manual::Unsweetened.3
/usr/share/man/man3/Moose::Meta::Attribute.3
/usr/share/man/man3/Moose::Meta::Attribute::Native.3
/usr/share/man/man3/Moose::Meta::Attribute::Native::Trait.3
/usr/share/man/man3/Moose::Meta::Attribute::Native::Trait::Array.3
/usr/share/man/man3/Moose::Meta::Attribute::Native::Trait::Bool.3
/usr/share/man/man3/Moose::Meta::Attribute::Native::Trait::Code.3
/usr/share/man/man3/Moose::Meta::Attribute::Native::Trait::Counter.3
/usr/share/man/man3/Moose::Meta::Attribute::Native::Trait::Hash.3
/usr/share/man/man3/Moose::Meta::Attribute::Native::Trait::Number.3
/usr/share/man/man3/Moose::Meta::Attribute::Native::Trait::String.3
/usr/share/man/man3/Moose::Meta::Class.3
/usr/share/man/man3/Moose::Meta::Class::Immutable::Trait.3
/usr/share/man/man3/Moose::Meta::Instance.3
/usr/share/man/man3/Moose::Meta::Method.3
/usr/share/man/man3/Moose::Meta::Method::Accessor.3
/usr/share/man/man3/Moose::Meta::Method::Augmented.3
/usr/share/man/man3/Moose::Meta::Method::Constructor.3
/usr/share/man/man3/Moose::Meta::Method::Delegation.3
/usr/share/man/man3/Moose::Meta::Method::Destructor.3
/usr/share/man/man3/Moose::Meta::Method::Meta.3
/usr/share/man/man3/Moose::Meta::Method::Overridden.3
/usr/share/man/man3/Moose::Meta::Mixin::AttributeCore.3
/usr/share/man/man3/Moose::Meta::Object::Trait.3
/usr/share/man/man3/Moose::Meta::Role.3
/usr/share/man/man3/Moose::Meta::Role::Application.3
/usr/share/man/man3/Moose::Meta::Role::Application::RoleSummation.3
/usr/share/man/man3/Moose::Meta::Role::Application::ToClass.3
/usr/share/man/man3/Moose::Meta::Role::Application::ToInstance.3
/usr/share/man/man3/Moose::Meta::Role::Application::ToRole.3
/usr/share/man/man3/Moose::Meta::Role::Attribute.3
/usr/share/man/man3/Moose::Meta::Role::Composite.3
/usr/share/man/man3/Moose::Meta::Role::Method.3
/usr/share/man/man3/Moose::Meta::Role::Method::Conflicting.3
/usr/share/man/man3/Moose::Meta::Role::Method::Required.3
/usr/share/man/man3/Moose::Meta::TypeCoercion.3
/usr/share/man/man3/Moose::Meta::TypeCoercion::Union.3
/usr/share/man/man3/Moose::Meta::TypeConstraint.3
/usr/share/man/man3/Moose::Meta::TypeConstraint::Class.3
/usr/share/man/man3/Moose::Meta::TypeConstraint::DuckType.3
/usr/share/man/man3/Moose::Meta::TypeConstraint::Enum.3
/usr/share/man/man3/Moose::Meta::TypeConstraint::Parameterizable.3
/usr/share/man/man3/Moose::Meta::TypeConstraint::Parameterized.3
/usr/share/man/man3/Moose::Meta::TypeConstraint::Registry.3
/usr/share/man/man3/Moose::Meta::TypeConstraint::Role.3
/usr/share/man/man3/Moose::Meta::TypeConstraint::Union.3
/usr/share/man/man3/Moose::Object.3
/usr/share/man/man3/Moose::Role.3
/usr/share/man/man3/Moose::Spec::Role.3
/usr/share/man/man3/Moose::Unsweetened.3
/usr/share/man/man3/Moose::Util.3
/usr/share/man/man3/Moose::Util::MetaRole.3
/usr/share/man/man3/Moose::Util::TypeConstraints.3
/usr/share/man/man3/Moose::Util::TypeConstraints::Builtins.3
/usr/share/man/man3/Test::Moose.3
/usr/share/man/man3/metaclass.3
/usr/share/man/man3/oose.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Moose/c173a21aa3da707ecef101c038841171903a78d2

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
