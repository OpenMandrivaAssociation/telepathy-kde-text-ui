%define rel 1

Summary:	Telepathy handler for Text Chats
Name:		telepathy-kde-text-ui
Version:	0.2.0
Release:	%mkrel %{rel}
Url:		https://projects.kde.org/projects/playground/network/telepathy/telepathy-text-ui
Source0:	ftp://ftp.gtlib.cc.gatech.edu/pub/kde/unstable/telepathy-kde/%version/src/%name-%version.tar.bz2
License:	GPLv2+
Group:		Graphical desktop/KDE
Obsoletes:      telepathy-chat-handler 
BuildRequires:	kdelibs4-devel
BuildRequires:	qt4-devel
BuildRequires:	telepathy-qt4-devel >= 0.7.1
BuildRequires:	shared-desktop-ontologies-devel
BuildRequires:  pkgconfig(telepathy-logger-0.2)
BuildRequires:  pkgconfig(QtGLib-2.0)
# Added on 2011/11/27
Provides: telepathy-text-ui = %version-%release
Obsoletes: telepathy-text-ui < 0.2.0-0


%description
Telepathy handler for Text Chats.

%files -f %name.lang
%{_kde_libdir}/kde4/kcm_telepathy_chat_appearance_config.so
%{_kde_libdir}/kde4/kcm_telepathy_chat_behavior_config.so
%{_kde_libdir}/kde4/libexec/adiumxtra-protocol-handler
%{_kde_libdir}/kde4/libexec/telepathy-kde-text-ui
%{_kde_services}/kcm_telepathy_chat_appearance_config.desktop
%{_kde_services}/kcm_telepathy_chat_behavior_config.desktop
%{_kde_libdir}/libktelepathy_chat_lib.so
%{_kde_appsdir}/ktelepathy/styles/
%{_kde_appsdir}/ktelepathy/template.html
%{_kde_appsdir}/telepathy-kde-text-ui
%{_kde_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.KDE.TextUi.service
%{_kde_services}/adiumxtra.protocol
%{_kde_datadir}/telepathy/clients/KDE.TextUi.client

#--------------------------------------------------------------------

%package devel
Summary:	Telepathy text chat handler
Group:		Graphical desktop/KDE
Requires:	%{name} = %{version}-%{release}
Obsoletes:      telepathy-chat-handler-devel
# Added on 2011/11/27
Obsoletes:      telepathy-text-ui-devel < 0.2.0-0
Provides:       telepathy-text-ui-devel = %version-%release  

%description devel
Telepathy text chat handler.

%files devel
%{_kde_includedir}/KDETelepathy/*

#--------------------------------------------------------------------

%prep
%setup -q 

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build
%find_lang %name
for i in "adiumxtra-protocol-handler" "ktelepathy_chat_lib" "telepathy-chat-window-config";
do 
%find_lang $i
cat $i.lang >> %name.lang
done


