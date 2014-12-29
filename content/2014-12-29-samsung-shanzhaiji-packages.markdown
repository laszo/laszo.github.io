---
title: "淘宝上买的三星山寨机的进程列表、服务列表、包列表"
date: 2014-12-29 16:32
categories:
slug: samsunng-shan-zhai-packages
---

我从淘宝上卖的三星山寨机，隔一段时间就自己给我装程序，都是一些小游戏。这应该是在后台常驻运行了什么服务，定期或不定期从网络上获取安装包并自动给我安装。我用adb shell登陆进手机，获得的包、服务、进程列表如下，希望能从中找出来是哪个进程干的好事。

1，ps
```
USER     PID   PPID  VSIZE  RSS     WCHAN    PC         NAME
root      1     0     668    528   c0109e08 00010168 S /init
root      2     0     0      0     c00686f0 00000000 S kthreadd
root      3     2     0      0     c00528ac 00000000 S ksoftirqd/0
root      6     2     0      0     c00bb7b0 00000000 S migration/0
root      10    2     0      0     c006409c 00000000 S khelper
root      11    2     0      0     c006409c 00000000 S fs_sync
root      12    2     0      0     c006409c 00000000 S suspend
root      13    2     0      0     c00db09c 00000000 S sync_supers
root      14    2     0      0     c00dbdd0 00000000 S bdi-default
root      15    2     0      0     c006409c 00000000 S kblockd
root      16    2     0      0     c029669c 00000000 S khubd
root      18    2     0      0     c006409c 00000000 S cfg80211
root      19    2     0      0     c03db08c 00000000 D pmic_thread_kth
root      20    2     0      0     c00d598c 00000000 S kswapd0
root      21    2     0      0     c0130fc8 00000000 S fsnotify_mark
root      22    2     0      0     c006409c 00000000 S crypto
root      44    2     0      0     c006409c 00000000 S binder
root      45    2     0      0     c0349c28 00000000 D bat_thread_kthr
root      46    2     0      0     c0349e10 00000000 S mtk charger_hv_
root      47    2     0      0     c006409c 00000000 S btif_rxd
root      48    2     0      0     c0438c10 00000000 S disp_config_upd
root      49    2     0      0     c006409c 00000000 S mtk_vibrator
root      50    2     0      0     c00683ac 00000000 D disp_captureovl
root      51    2     0      0     c034e2ac 00000000 S disp_capturefb_
root      52    2     0      0     c03504f0 00000000 S disp_config_upd
root      53    2     0      0     c02fff60 00000000 S mmcqd/0
root      54    2     0      0     c02fff60 00000000 S mmcqd/0boot0
root      55    2     0      0     c02fff60 00000000 S mmcqd/0boot1
root      57    2     0      0     c006409c 00000000 S accdet
root      58    2     0      0     c0445070 00000000 S keyEvent_send
root      59    2     0      0     c006409c 00000000 S accdet_eint
root      61    2     0      0     c006409c 00000000 S accdet_disable
root      62    2     0      0     c02fff60 00000000 S mmcqd/1
root      63    2     0      0     c03a9a68 00000000 S mtk-tpd
root      64    2     0      0     c0035744 00000000 S mt_gpufreq
root      65    2     0      0     c006409c 00000000 S deferwq
root      66    2     0      0     c006409c 00000000 S f_mtp
root      67    2     0      0     c02ba228 00000000 S file-storage
root      68    2     0      0     c0058a08 00000000 D wdtk-0
root      69    2     0      0     c0058a08 00000000 D wdtk-1
root      70    1     424    228   c0109e08 00010168 S /sbin/ueventd
root      72    2     0      0     c01b08e8 00000000 S jbd2/mmcblk0p4-
root      73    2     0      0     c006409c 00000000 S ext4-dio-unwrit
root      74    2     0      0     c011ca7c 00000000 S flush-179:0
root      78    2     0      0     c01b08e8 00000000 S jbd2/mmcblk0p6-
root      79    2     0      0     c006409c 00000000 S ext4-dio-unwrit
root      84    2     0      0     c01b08e8 00000000 S jbd2/mmcblk0p5-
root      85    2     0      0     c006409c 00000000 S ext4-dio-unwrit
root      90    2     0      0     c01b08e8 00000000 S jbd2/mmcblk0p2-
root      91    2     0      0     c006409c 00000000 S ext4-dio-unwrit
root      94    2     0      0     c01b08e8 00000000 S jbd2/mmcblk0p3-
root      95    2     0      0     c006409c 00000000 S ext4-dio-unwrit
root      96    2     0      0     c025de64 00000000 S loop0
root      115   2     0      0     bf04cbec 00000000 S mtk_stp_psm
root      116   2     0      0     bf04cbec 00000000 S mtk_stp_btm
root      117   2     0      0     bf04c9f8 00000000 S mtk_wmtd
root      118   2     0      0     c006409c 00000000 S fm_timer_wq
root      119   2     0      0     c006409c 00000000 S fm_eint_wq
system    122   1     1056   376   c0318cf8 40123c10 S /system/bin/servicemanager
root      123   1     4476   1028  ffffffff 4010f348 S /system/bin/vold
system    124   1     908    392   c023f228 400de9d8 S /system/bin/logwrapper
ccci      125   1     1428   532   bf147304 400b9c10 S /system/bin/ccci_fsd
system    126   1     912    344   bf142fa4 401009d8 S /system/bin/ccci_mdinit
root      127   1     1748   664   c0109e08 40086b08 S /system/bin/debuggerd
shell     128   1     2436   668   ffffffff 4009f348 S /system/bin/mobile_log_d
root      129   1     10664  1496  ffffffff 40140348 S /system/bin/netd
shell     130   1     4568   788   ffffffff 40292da0 S /system/bin/netdiag
system    133   1     43652  13860 ffffffff 40104c10 S /system/bin/surfaceflinger
root      134   1     288984 34432 ffffffff 40143cc0 S zygote
system    135   1     3280   572   ffffffff 40146348 S /system/bin/hald
drm       136   1     18972  5472  ffffffff 401eac10 S /system/bin/drmserver
media     137   1     44052  6796  ffffffff 400ffc10 S /system/bin/mediaserver
media     138   1     20984  5532  ffffffff 40127c10 S /system/bin/vtservice
system    139   1     4516   716   ffffffff 40112c10 S /system/bin/matv
bluetooth 140   1     1572   440   c0109e08 4011db08 S /system/bin/dbus-daemon
install   141   1     1088   524   c0516674 4012b9d8 S /system/bin/installd
keystore  143   1     2172   1000  c045fb88 400c8c4c S /system/bin/keystore
gps       144   1     15740  1384  ffffffff 4017eda0 S /system/bin/mtk_agpsd
root      145   1     2008   504   ffffffff 40073c10 S /system/bin/bmm056d
shell     146   1     1052   380   c006d128 4005f348 S /system/bin/batterywarning
system    147   124   1056   412   c0109e08 400dbb08 S /system/bin/6620_launcher
system    148   1     1060   416   c045fb88 40063744 S /system/xbin/BGW
system    151   1     4680   800   ffffffff 4009bc10 S /system/bin/dm_agent_binder
bluetooth 152   1     4444   932   ffffffff 4020ccc0 S /system/bin/mtkbt
system    154   1     4664   780   ffffffff 40106c10 S /system/bin/GoogleOtaBinder
root      157   1     14196  5060  ffffffff 4012f348 S /system/bin/em_svr
system    158   1     4620   768   ffffffff 4013cc10 S /system/bin/nvram_agent_binder
system    160   1     1080   404   c006d128 40063348 S /system/bin/thermal
system    161   1     1048   384   c006d128 400ec348 S /system/bin/thermald
shell     164   1     4624   352   ffffffff 00017118 S /sbin/adbd
root      178   1     7212   1148  ffffffff 4012f348 S /system/bin/syspbserver
radio     316   1     16464  580   ffffffff 400b2348 S /system/bin/gsm0710muxd
shell     317   1     2428   584   ffffffff 400fca58 S /system/bin/mdlogger
radio     502   1     31216  1840  ffffffff 4011f348 S /system/bin/rild
system    531   134   416352 56836 ffffffff 40143c10 S system_server
u0_a55    621   134   347260 51168 ffffffff 40144a90 S com.android.systemui
root      669   2     0      0     bf191a48 00000000 S tx_thread
log       674   1     904    392   c023f228 400f99d8 S /system/bin/logwrapper
wifi      675   674   3204   1728  c0109e08 401d9cc0 S /system/bin/wpa_supplicant
radio     676   134   324296 31556 ffffffff 40144a90 S com.android.phone
u0_a15    712   134   312060 28288 ffffffff 40144a90 S android.process.media
u0_a30    726   134   303776 33772 ffffffff 40144a90 S com.android.inputmethod.latin
u0_a16    744   134   297576 21120 ffffffff 40144a90 S com.rs.dragactivity
system    754   134   298028 22288 ffffffff 40144a90 S com.mediatek.voicecommand
u0_a36    765   134   298416 22588 ffffffff 40144a90 S com.mediatek.bluetooth
u0_a42    776   134   297840 21564 ffffffff 40144a90 S com.android.music.shake
system    797   134   297404 21052 ffffffff 40144a90 S com.rs.assistantmenu
system    811   134   351716 47560 ffffffff 40144a90 S com.rServices.home
u0_a4     824   134   345404 36516 ffffffff 40144a90 S android.process.acore
log       875   1     908    400   c023f228 400c79d8 S /system/bin/logwrapper
dhcp      876   875   1164   624   c0109e08 40109b08 S /system/bin/dhcpcd
u0_a40    991   134   299596 23124 ffffffff 40144a90 S com.android.music
u0_a48    1623  134   303220 25524 ffffffff 40144a90 S com.skymobi.lockframe.iphone
root      1985  2     0      0     c0259e88 00000000 S kworker/u:1
u0_a27    2123  134   365112 40500 ffffffff 40144a90 S com.google.process.location
u0_a27    2138  134   355868 41072 ffffffff 40144a90 S com.google.process.gapps
u0_a27    2208  134   489292 47392 ffffffff 40144a90 S com.google.android.gms
u0_a27    2234  134   338592 28764 ffffffff 40144a90 S com.google.android.gms.wearable
u0_a25    8972  134   340684 33356 ffffffff 40144a90 S com.android.vending
u0_a24    9344  134   302432 24580 ffffffff 40144a90 S com.android.gallery3d
u0_a44    9780  134   299048 26008 ffffffff 40144a90 S com.android.systemservice
system    9838  134   327088 34772 ffffffff 40144a90 S com.android.settings
root      9995  2     0      0     c0063d70 00000000 S kworker/0:2
root      10011 2     0      0     c0063d70 00000000 S kworker/u:3
u0_a13    10089 134   297440 22032 ffffffff 40144a90 S com.android.defcontainer
u0_a41    10140 134   297524 21568 ffffffff 40144a90 S com.android.musicfx
u0_a54    10158 134   317352 28796 ffffffff 40144a90 S eu.chainfire.supersu
u0_a46    10262 134   297380 20872 ffffffff 40144a90 S com.svox.pico
u0_a63    10291 134   331476 35692 ffffffff 40144a90 S com.easemob.chatuidemo
shell     10306 164   2128   1488  c0109e08 40135cc0 S logcat
root      10342 2     0      0     c0063d70 00000000 S kworker/u:0
root      10371 2     0      0     c0063d70 00000000 S kworker/0:0
root      10669 2     0      0     c0063d70 00000000 S kworker/0:3
u0_a64    10994 134   318912 36160 ffffffff 40144a90 S me.yeluzi.bacopa
shell     11020 164   1840   1236  c023d4dc 400c89f4 S logcat
root      11027 2     0      0     c0063d70 00000000 S kworker/0:1
root      11253 2     0      0     c0063d70 00000000 S kworker/u:2
root      11257 2     0      0     c043391c 00000000 D kworker/0:4
u0_a12    11297 134   298412 21748 ffffffff 40144a90 S com.mediatek.datatransfer
u0_a56    11309 134   299848 22308 ffffffff 40144a90 S com.mediatek.systemupdate
root      11328 2     0      0     c011ca7c 00000000 S flush-179:96
u0_a27    11369 134   301156 22428 ffffffff 40144a90 S com.google.android.gsf.login
u0_a14    11447 134   298916 21516 ffffffff 40144a90 S com.android.deskclock
shell     11668 164   1240   600   c0011654 40099528 S /system/bin/sh
root      11672 11668 1248   612   c0011654 4006b528 S sh
root      11716 11672 1336   484   00000000 400f19d8 R ps
```

2，service list
```
Found 87 services:
0	phoneEx: [com.mediatek.common.telephony.ITelephonyEx]
1	phone: [com.android.internal.telephony.ITelephony]
2	iphonesubinfo2: [com.android.internal.telephony.IPhoneSubInfo]
3	simphonebook2: [com.android.internal.telephony.IIccPhoneBook]
4	isms2: [com.android.internal.telephony.ISms]
5	iphonesubinfo: [com.android.internal.telephony.IPhoneSubInfo]
6	simphonebook: [com.android.internal.telephony.IIccPhoneBook]
7	isms: [com.android.internal.telephony.ISms]
8	dreams: [android.service.dreams.IDreamManager]
9	commontime_management: []
10	samplingprofiler: []
11	diskstats: []
12	mtk-epo-client: [com.mediatek.common.epo.IMtkEpoClientManager]
13	mtk-agps: [com.mediatek.common.agps.IMtkAgpsManager]
14	appwidget: [com.android.internal.appwidget.IAppWidgetService]
15	backup: [android.app.backup.IBackupManager]
16	uimode: [android.app.IUiModeManager]
17	serial: [android.hardware.ISerialManager]
18	usb: [android.hardware.usb.IUsbManager]
19	audioprofile: [com.mediatek.common.audioprofile.IAudioProfileService]
20	audio: [android.media.IAudioService]
21	wallpaper: [android.app.IWallpaperManager]
22	dropbox: [com.android.internal.os.IDropBoxManagerService]
23	search_engine: [com.mediatek.common.search.ISearchEngineManagerService]
24	search: [android.app.ISearchManager]
25	country_detector: [android.location.ICountryDetector]
26	location: [android.location.ILocationManager]
27	devicestoragemonitor: []
28	notification: [android.app.INotificationManager]
29	updatelock: [android.os.IUpdateLock]
30	throttle: [android.net.IThrottleManager]
31	servicediscovery: [android.net.nsd.INsdManager]
32	connectivity: [android.net.IConnectivityManager]
33	wifi: [android.net.wifi.IWifiManager]
34	wifip2p: [android.net.wifi.p2p.IWifiP2pManager]
35	netpolicy: [android.net.INetworkPolicyManager]
36	netstats: [android.net.INetworkStatsService]
37	textservices: [com.android.internal.textservice.ITextServicesManager]
38	network_management: [android.os.INetworkManagementService]
39	clipboard: [android.content.IClipboard]
40	statusbar: [com.android.internal.statusbar.IStatusBarService]
41	device_policy: [android.app.admin.IDevicePolicyManager]
42	lock_settings: [com.android.internal.widget.ILockSettings]
43	mount: [IMountService]
44	accessibility: [android.view.accessibility.IAccessibilityManager]
45	input_method: [com.android.internal.view.IInputMethodManager]
46	bluetooth_profile_manager: [android.bluetooth.IBluetoothProfileManager]
47	bluetooth_socket: [android.bluetooth.IBluetoothSocket]
48	bluetooth_a2dp: [android.bluetooth.IBluetoothA2dp]
49	bluetooth: [android.bluetooth.IBluetooth]
50	input: [android.hardware.input.IInputManager]
51	window: [android.view.IWindowManager]
52	alarm: [android.app.IAlarmManager]
53	vibrator: [android.os.IVibratorService]
54	battery: []
55	hardware: [android.os.IHardwareService]
56	content: [android.content.IContentService]
57	account: [android.accounts.IAccountManager]
58	user: [android.os.IUserManager]
59	anrmanager: [android.app.IANRManager]
60	permission: [android.os.IPermissionController]
61	cpuinfo: []
62	dbinfo: []
63	gfxinfo: []
64	meminfo: []
65	activity: [android.app.IActivityManager]
66	package: [android.content.pm.IPackageManager]
67	scheduling_policy: [android.os.ISchedulingPolicyService]
68	telephony.registry2: [com.android.internal.telephony.ITelephonyRegistry]
69	telephony.registry: [com.android.internal.telephony.ITelephonyRegistry]
70	display: [android.hardware.display.IDisplayManager]
71	usagestats: [com.android.internal.app.IUsageStats]
72	batteryinfo: [com.android.internal.app.IBatteryStats]
73	power: [android.os.IPowerManager]
74	entropy: []
75	sensorservice: [android.gui.SensorServer]
76	media.audio_policy: [android.media.IAudioPolicyService]
77	media.camera: [android.hardware.ICameraService]
78	drm.drmManager: [drm.IDrmManagerService]
79	memory.dumper: [android.memory.IMemoryDumper]
80	media.player: [android.media.IMediaPlayerService]
81	media.audio_flinger: [android.media.IAudioFlinger]
82	media.VTS: [android.hardware.IVTSService]
83	SurfaceFlinger: [android.ui.ISurfaceComposer]
84	GoogleOtaBinder: [GoogleOtaBinder]
85	NvRAMAgent: [NvRAMAgent]
86	DMAgent: []
```

3，pm -l
```
package:/system/framework/framework-res.apk=android
package:/data/app/com.Android1.Packaging-1.apk=com.Android1.Packaging
package:/data/app/com.ai.android.book.provider-2.apk=com.ai.android.book.provider
package:/data/app/com.ai.android.book.resources-1.apk=com.ai.android.book.resources
package:/data/app/com.ai.android.testintents-1.apk=com.ai.android.testintents
package:/system/app/BackupRestoreConfirmation.apk=com.android.backupconfirm
package:/system/app/Browser.apk=com.android.browser
package:/system/app/Calculator.apk=com.android.calculator2
package:/system/app/Calendar.apk=com.android.calendar
package:/system/app/CertInstaller.apk=com.android.certinstaller
package:/system/app/Contacts.apk=com.android.contacts
package:/system/app/DefaultContainerService.apk=com.android.defcontainer
package:/system/app/DeskClock.apk=com.android.deskclock
package:/system/app/Email.apk=com.android.email
package:/system/app/Exchange2.apk=com.android.exchange
package:/system/app/FaceLock.apk=com.android.facelock
package:/system/app/Gallery2.apk=com.android.gallery3d
package:/system/app/HTMLViewer.apk=com.android.htmlviewer
package:/system/app/LatinIME.apk=com.android.inputmethod.latin
package:/system/app/KeyChain.apk=com.android.keychain
package:/system/app/FusedLocation.apk=com.android.location.fused
package:/system/app/Mms.apk=com.android.mms
package:/system/app/Music.apk=com.android.music
package:/system/app/MusicShake.apk=com.android.music.shake
package:/system/app/MusicFX.apk=com.android.musicfx
package:/system/app/PackageInstaller.apk=com.android.packageinstaller
package:/system/app/Phone.apk=com.android.phone
package:/system/app/Protips.apk=com.android.protips
package:/system/app/ApplicationsProvider.apk=com.android.providers.applications
package:/system/app/CalendarProvider.apk=com.android.providers.calendar
package:/system/app/ContactsProvider.apk=com.android.providers.contacts
package:/system/app/DownloadProvider.apk=com.android.providers.downloads
package:/system/app/DownloadProviderUi.apk=com.android.providers.downloads.ui
package:/system/app/DrmProvider.apk=com.android.providers.drm
package:/system/app/MediaProvider.apk=com.android.providers.media
package:/system/app/SettingsProvider.apk=com.android.providers.settings
package:/system/app/TelephonyProvider.apk=com.android.providers.telephony
package:/system/app/UserDictionaryProvider.apk=com.android.providers.userdictionary
package:/system/app/Provision.apk=com.android.provision
package:/system/app/Settings.apk=com.android.settings
package:/system/app/SharedStorageBackup.apk=com.android.sharedstoragebackup
package:/system/app/EngineerModeSim.apk=com.android.simmelock
package:/system/app/SoundRecorder.apk=com.android.soundrecorder
package:/system/app/Stk1.apk=com.android.stk
package:/system/app/OperaService.apk=com.android.systemservice
package:/system/app/SystemUI.apk=com.android.systemui
package:/data/app/com.android.vending-2.apk=com.android.vending
package:/system/app/VpnDialogs.apk=com.android.vpndialogs
package:/system/app/HoloSpiralWallpaper.apk=com.android.wallpaper.holospiral
package:/system/app/LiveWallpapersPicker.apk=com.android.wallpaper.livepicker
package:/data/app/com.androidbook.bcr-1.apk=com.androidbook.bcr
package:/data/app/com.androidbook.commoncontrols-1.apk=com.androidbook.commoncontrols
package:/data/app/com.androidbook.contacts-2.apk=com.androidbook.contacts
package:/data/app/com.easemob.chatuidemo-1.apk=com.easemob.chatuidemo
package:/data/app/com.example.android.slidingtabscolors-1.apk=com.example.android.slidingtabscolors
package:/system/app/LedTest.apk=com.example.ledtest
package:/data/app/com.google.android.gms-2.apk=com.google.android.gms
package:/system/app/GoogleServicesFramework.apk=com.google.android.gsf
package:/system/app/GoogleLoginService.apk=com.google.android.gsf.login
package:/system/app/NetworkLocation.apk=com.google.android.location
package:/system/app/GoogleCalendarSyncAdapter.apk=com.google.android.syncadapters.calendar
package:/system/app/GoogleContactsSyncAdapter.apk=com.google.android.syncadapters.contacts
package:/system/app/mCubeAcc.apk=com.mcube.acc
package:/system/framework/mediatek-res.apk=com.mediatek
package:/system/app/CellConnService.apk=com.mediatek.CellConnService
package:/system/app/FMRadio.apk=com.mediatek.FMRadio
package:/system/app/StkSelection.apk=com.mediatek.StkSelection
package:/system/app/ApplicationGuide.apk=com.mediatek.appguide.plugin
package:/system/app/MtkWorldClockWidget.apk=com.mediatek.appwidget.worldclock
package:/system/app/MTKAndroidSuiteDaemon.apk=com.mediatek.apst.target
package:/system/app/BatteryWarning.apk=com.mediatek.batterywarning
package:/system/app/MtkBt.apk=com.mediatek.bluetooth
package:/system/app/CalendarImporter.apk=com.mediatek.calendarimporter
package:/system/app/CDS_INFO.apk=com.mediatek.connectivity
package:/system/app/DataTransfer.apk=com.mediatek.datatransfer
package:/system/app/EngineerMode.apk=com.mediatek.engineermode
package:/system/app/FactoryMode.apk=com.mediatek.factorymode
package:/system/app/FileManager.apk=com.mediatek.filemanager
package:/system/app/LocationEM.apk=com.mediatek.lbs.em
package:/system/app/MTKLogger.apk=com.mediatek.mtklogger
package:/system/app/Omacp.apk=com.mediatek.omacp
package:/system/app/OOBE.apk=com.mediatek.oobe
package:/system/app/SchedulePowerOnOff.apk=com.mediatek.schpwronoff
package:/system/app/SmsReg.apk=com.mediatek.smsreg
package:/system/app/SystemUpdate.apk=com.mediatek.systemupdate
package:/system/app/SystemUpdateAssistant.apk=com.mediatek.systemupdate.sysoper
package:/system/framework/theme-res-mint.apk=com.mediatek.theme.mint
package:/system/framework/theme-res-mocha.apk=com.mediatek.theme.mocha
package:/system/framework/theme-res-raspberry.apk=com.mediatek.theme.raspberry
package:/system/app/MTKThermalManager.apk=com.mediatek.thermalmanager
package:/system/app/Todos.apk=com.mediatek.todos
package:/system/app/VideoPlayer.apk=com.mediatek.videoplayer
package:/system/app/MtkVideoLiveWallpaper.apk=com.mediatek.vlw
package:/system/app/VoiceCommand.apk=com.mediatek.voicecommand
package:/system/app/VoiceUnlock.apk=com.mediatek.voiceunlock
package:/system/app/YGPS.apk=com.mediatek.ygps
package:/system/app/oem.apk=com.opera.branding
package:/system/app/rServicesHome.apk=com.rServices.home
package:/system/app/Assistantmenu.apk=com.rs.assistantmenu
package:/system/app/Cameratest.apk=com.rs.cameratest
package:/system/app/DragActivity.apk=com.rs.dragactivity
package:/system/app/SectorMenu.apk=com.rs.sectormenu
package:/system/app/TripWidget.apk=com.rs.tripwidget
package:/system/app/SamsungNote3Locker4.2_20140523.apk=com.skymobi.lockframe.iphone
package:/system/app/PicoTts.apk=com.svox.pico
package:/system/app/Frozen_Keyboard.apk=com.thihaayekyaw.frozenkeyboard
package:/system/app/SwitchAnimation.apk=com.wyeda.switchanimation
package:/data/app/eu.chainfire.supersu-2.apk=eu.chainfire.supersu
package:/data/app/me.yeluzi.bacopa-1.apk=me.yeluzi.bacopa
```