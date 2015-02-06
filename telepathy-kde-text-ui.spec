%define srcname ktp-text-ui

Summary:	Telepathy handler for Text Chats
Name:		telepathy-kde-text-ui
Version:	0.5.1
Release:	2
Url:		https://projects.kde.org/projects/playground/network/telepathy/telepathy-text-ui
Source0:	ftp://ftp.gtlib.cc.gatech.edu/pub/kde/unstable/telepathy-kde/%version/src/%srcname-%version.tar.bz2
License:	GPLv2+
Group:		Networking/Instant messaging
BuildRequires:	telepathy-kde-common-internals-devel >= %{version}
BuildRequires:	pkgconfig(shared-desktop-ontologies)
BuildRequires:	pkgconfig(telepathy-logger-0.2)
BuildRequires:	pkgconfig(QtGLib-2.0)
BuildRequires:	pkgconfig(TelepathyLoggerQt4)
BuildRequires:	boost-devel
BuildRequires:	fontconfig

# Added on 2011/11/27
Obsoletes:	telepathy-text-ui < 0.2.0-0
Obsoletes:	telepathy-chat-handler 

Requires:	telepathy-kde-common-internals-core
Requires:	telepathy-kde-send-file
# Spell check support
Requires:	iso-codes


%description
Telepathy handler for Text Chats.

%files -f ktp-text-ui.lang
%{_kde_bindir}/ktp-log-viewer
%{_kde_libdir}/libktpchat.so
%{_kde_libdir}/kde4/kcm_ktp_chat_messages.so
%{_kde_libdir}/kde4/ktptextui_message_filter_emoticons.so
%{_kde_libdir}/kde4/ktptextui_message_filter_images.so
%{_kde_libdir}/kde4/kcm_ktp_chat_appearance.so
%{_kde_libdir}/kde4/kcm_ktp_chat_behavior.so
%{_kde_libdir}/kde4/libexec/ktp-adiumxtra-protocol-handler
%{_kde_libdir}/kde4/libexec/ktp-text-ui
%{_kde_libdir}/kde4/imports/org/kde/telepathy/chat/qmldir
%{_kde_libdir}/kde4/imports/org/kde/telepathy/chat/libktpchatqmlplugin.so
%{_kde_appsdir}/ktelepathy/styles/
%{_kde_appsdir}/ktelepathy/Template.html
%{_kde_appsdir}/ktp-text-ui
%{_kde_appsdir}/plasma/plasmoids/org.kde.ktp-chatplasmoid
%{_kde_applicationsdir}/ktp-log-viewer.desktop
%{_kde_services}/adiumxtra.protocol
%{_kde_services}/kcm_ktp_chat_appearance.desktop
%{_kde_services}/kcm_ktp_chat_behavior.desktop
%{_kde_services}/kcm_ktp_chat_messages.desktop
%{_kde_services}/ktptextui_message_filter_emoticons.desktop
%{_kde_services}/ktptextui_message_filter_images.desktop
%{_kde_services}/plasma-applet-ktpchat.desktop
%{_kde_servicetypes}/ktptxtui_message_filter.desktop
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.KTp.TextUi.service
%{_datadir}/telepathy/clients/KTp.TextUi.client

#------------------------------------------------------------------------------

%package devel
Summary:	Telepathy text chat handler
Group:		Graphical desktop/KDE
Requires:	%{name} = %{version}-%{release}
Obsoletes:	telepathy-chat-handler-devel
# Added on 2011/11/27
Obsoletes:	telepathy-text-ui-devel < 0.2.0-0
Provides:	telepathy-text-ui-devel = %version-%release  

%description devel
Telepathy text chat handler.

%files devel
%{_kde_includedir}/KTp/*

#------------------------------------------------------------------------------

%prep
%setup -q -n %srcname-%version

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build
%find_lang ktp-text-ui --all-name
