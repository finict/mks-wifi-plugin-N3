# MKS WiFi plugin with N3P thumbnail support #
Tested on `Neptune 3 Pro` with `Cura5.3.1` and `MKSWiFiPlugin1.4.2` (should work on Plus/Max)

![N3P](https://github.com/finict/mks-wifi-plugin-N3/assets/16084632/d0123695-6264-4e49-860a-ba05b2224e5b)  
Model by [3dbenchy](https://www.3dbenchy.com/download/)

## How to install ##
If you already installed original MKS WiFi Plugin jump to instruction 3

1. Install MKS WiFi plugin at Cura Marketplace
2. Restart Cura (Required)
3. Download ELEGOO Cura **$\color{#ff0000}{\textsf{Windows version}}$** [here](https://www.elegoo.com/en-jp/pages/3d-printing-user-support) (Slicing Software section)
4. Open downloaded exe binary **$\color{#ff0000}{\textsf{as archive}}$** use with 7zip etc.
5. find specific binary in `[ARCHIVE]/plugins/MKS Plugin` folder
    1. Windows `ColPic_X64.dll`
    2. Linux `libColPic.so`
    3. Mac `libColPic.dylib`
6. Copy the above binary to plugin folder in Cura
    1. Windows `%appdata%/cura/[VERSION]/plugins/MKSWiFiPlugin/MKSWiFiPlugin`
    2. Linux `-`
    3. Mac `-`
8. Download [MKSPreview.py](https://github.com/finict/mks-wifi-plugin-N3/releases/latest) in this repository
9. Copy the MKSPreview.py to plugin folder in Cura (Overwrite)
10. change plugin setting `Settings > Printer > Manage Printers`
    1. Select `Neptune 3 Pro/Plus/Max`
    2. Push `MKS WiFi Plugin` button
    3. Check the `MKS WiFi Plugin is active for this printer`
    4. Move `Preview settings` tab
        1. Check `Screenshot support`
        2. Printer model to `Custom`
        3. Simage to `160`
        4. Gimage to `200`
11. Restart Cura

Have a nice print!

<br><br><br><br>
Original readme bellow

---
# MKS WiFi plugin #

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=Jeredian_mks-wifi-plugin&metric=alert_status)](https://sonarcloud.io/dashboard?id=Jeredian_mks-wifi-plugin)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=Jeredian_mks-wifi-plugin&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=Jeredian_mks-wifi-plugin)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=Jeredian_mks-wifi-plugin&metric=bugs)](https://sonarcloud.io/dashboard?id=Jeredian_mks-wifi-plugin)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=Jeredian_mks-wifi-plugin&metric=code_smells)](https://sonarcloud.io/dashboard?id=Jeredian_mks-wifi-plugin)

MKS WiFi plugin for Cura developed by [Makerbase](https://github.com/makerbase-mks), [Jeredian](https://github.com/Jeredian) and [Elkin-Vasily](https://github.com/Elkin-Vasily) and it was originaly migrated from [https://github.com/makerbase-mks/Software](https://github.com/makerbase-mks/Software "https://github.com/makerbase-mks/Software") after V4.4 version.

Using the plugin with Cura, you can:
  - Connect Cura to the MKS Robin WiFi and MKS TFT WiFi;
  - Control your 3D printer wirelessly with Cura;
  - Transfer .gcode files to a printer with 100kbyte/s speed;
  - Get preview on 3D printer srceen when using MKS Robin TFT35 or MKS TFT35 LCD.

## Installation ##

Marketplace:
  - Plugin is available through the Cura Marketplace as the MKS Wifi Plugin.

Manually with .curapackage:
  - Download .curapackage file of the selected [release](https://github.com/Jeredian/mks-wifi-plugin/releases);
  - Open Cura on the Prepare tab;
  - Drag and drop .curapackage on this tab.

Manually with sources:
  - Download or clone this repository;
  - Open Cura configuration folder. It can be found via Help -> Show Configuration Folder inside Cura;
  - Copy folder into [Cura configuration folder]/plugins/ ;
  - Restart Cura.
  
Notes:
  - Latest version of MKS WiFi plugin is only available for Cura 5.0 or higher version;
  - For Cura versions 4.7-4.13.1 please manually install version [1.3.2](https://github.com/Jeredian/mks-wifi-plugin/releases/tag/1.3.2);
  - For Cura versions 4.5-4.6 please manually install version [1.2.2](https://github.com/Jeredian/mks-wifi-plugin/releases/tag/1.2.2).

## Troubleshooting ##

Please [create a new GitHub issue](https://github.com/Jeredian/mks-wifi-plugin/issues/new/choose) and provide all details according to the template.

Or you can ask a question in our [Telegram group](https://t.me/mks_wifi_plugin_reception).

## Translation ##

To create new translation, or improve existing one, please check [automatic translation guide](https://github.com/Jeredian/mks-wifi-plugin/wiki/Automatic-Translation) or [manual translation guide](https://github.com/Jeredian/mks-wifi-plugin/wiki/Manual-Translation).

## Funding ##
 The development of this plugin can be sponsored via [Paypal](https://www.paypal.me/PaulHelgesson "https://www.paypal.me/PaulHelgesson") or [Yoomoney](https://yoomoney.ru/to/410012506859451)
