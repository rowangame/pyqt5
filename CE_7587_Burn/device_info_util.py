# -*- coding: UTF-8 -*-
# @Time    : 2024/10/1210:52
# @Author  : xielunguo
# @Email   : xielunguo@cosonic.com
# @File    : device_info_util.py
# @IDE     : PyCharm
from language_util import Language_Util
from serial_manager import Serial_Manager


class Dev_Info_Util:
    cur_dev_version: str = ""

    cur_dev_mac: str = ""

    cur_dev_record = None

    @classmethod
    def clearCurDevInfo(cls):
        cls.cur_dev_record = ""
        cls.cur_dev_mac = ""
        cls.cur_dev_record = None

    @classmethod
    def getDevInfo(cls, com: str):
        """
        获取设备信息
        :param com:
            串口号
        :return:
            state: True(成功)
            data: 版本号,Mac地址
            msg: 提示信息
        """
        CMD_S = ["TL_ATS_IN\n", "TL_GET_VER\n", "TL_GET_BTMAC\n", "TL_ATS_OFF\n"]

        boSuccess = Serial_Manager.openSerial(com)
        if not boSuccess:
            return False, [], Language_Util.getValue("dev_open_port_fail")

        try:
            lstRlt = []
            state, tmpLstRes = Serial_Manager.sendATCommand(CMD_S[0])
            if (not state) or ("SUCCESS" not in tmpLstRes[0]):
                return False, [], Language_Util.getValue("dev_enter_ats_fail")

            state, tmpLstRes = Serial_Manager.sendATCommand(CMD_S[1])
            if (not state) or ("SUCCESS" not in tmpLstRes[0]):
                return False, [], Language_Util.getValue("dev_get_ver_fail")
            # 解析版本号
            VER_TAG = "VER="
            tmpStr: str = tmpLstRes[0]
            tmpIdx = tmpStr.find(VER_TAG)
            tmpVer = tmpStr[tmpIdx + len(VER_TAG): len(tmpStr)].strip()
            lstRlt.append(tmpVer)

            state, tmpLstRes = Serial_Manager.sendATCommand(CMD_S[2])
            if (not state) or ("SUCCESS" not in tmpLstRes[0]):
                return False, [], Language_Util.getValue("dev_get_mac_fail")
            # 解析Mac地址
            MAC_TAG = "BTMAC="
            tmpStr: str = tmpLstRes[0]
            tmpIdx = tmpStr.find(MAC_TAG)
            tmpMac = tmpStr[tmpIdx + len(MAC_TAG): len(tmpStr)].strip()
            lstRlt.append(tmpMac)

            # 退出工厂模式
            state, tmpLstRes = Serial_Manager.sendATCommand(CMD_S[3])
            if (not state) or ("SUCCESS" not in tmpLstRes[0]):
                print(Language_Util.getValueEx("dev_quit_ats_fail", Language_Util.CODE_EN))

            return True, lstRlt, "Success"
        except Exception as e:
            print(f"{Language_Util.getValueEx('dev_get_info_fail', Language_Util.CODE_EN)}:" + repr(e))
        finally:
            Serial_Manager.closeSerial()
        return False, [], "Fail"
