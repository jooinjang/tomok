import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS244005_030503_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 24 40 05 3.5.3 (1)'
    ref_date = '2018-08-30'
    doc_date = '2023-11-07'
    title = '지진격리받침의 품질'

    description = """
    교량받침
    3. 시공
    3.3 포트받침 및 디스크받침
    3.5.3 품질기준
    (1)
    """
    content = """
    #### 3.3.2 표본선정과 시험
    (1) 지진격리받침의 전수 품질시험에 의해 측정한 평균 전단유효강성()은 설계값의 ±10% 이내이어야 하고, 각각의 전단유효강성은 설계값의 ±20% 이내이어야 한다. 또한, 평균 EDC 값은 설계값의 –15% 이상이어야 하고 각각의 EDC 값은 설계값의 –25% 이상이어야 한다.
    표 3.5-1 지진격리받침 전단유효강성과 EDC의 품질 기준
    \begin{table}[]
    \begin{tabular}{lcc}
    구분                        & \multicolumn{1}{l}{keff}   & \multicolumn{1}{l}{EDC}  \\
    \multicolumn{1}{c}{평균값}   & ±10%                       & -15% 이상                  \\
    \multicolumn{1}{c}{개체차}   & ±20%                       & -25% 이상                  \\
    \multicolumn{3}{l}{주 1) EDC(Energy Dissipation per Cycle):지진격리장치의 하중-변위 이력곡선의 면적}
    \end{tabular}
    \end{table}
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 지진격리받침의 품질];
    B["KCS 24 40 05 3.5.3 (1)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 05 3.5.3 (1)"])

    subgraph Variable_def
    VarIn1[/입력변수: 평균 전단유효강성/];
    VarIn2[/입력변수: 각각의 전단유효강성/];
    VarIn3[/입력변수: 설계 전단유효강성/];
    VarIn4[/입력변수: 평균 EDC/];
    VarIn5[/입력변수: 각각의 EDC/];
    VarIn6[/입력변수: 설계 EDC/];
    VarIn1 & VarIn2 & VarIn3 ~~~ VarIn4 & VarIn5 & VarIn6
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"설계 전단유효강성* 0.9 <평균 전단유효강성 < 설계 전단유효강성* 1.1 \n 설계 전단유효강성* 0.8 <각각의 전단유효강성 < 설계 전단유효강성* 1.2 \n 평균 EDC ≥ 설계 EDC * 0.85\n각각의 EDC ≥ 설계 EDC * 0.75\n."}
    C --> End([Pass or Fail])
    """

    @rule_method

    def quality_seismic_bearing(fIAveKef,fIEacKef,fIDesKef,fIAveEdc,fIEacEdc,fIDesEdc) -> RuleUnitResult:
        """
        Args:
            fIAveKef (float): 평균 전단유효강성
            fIEacKef (float): 각각의 전단유효강성
            fIDesKef (float): 설계 전단유효강성
            fIAveEdc (float): 평균 EDC
            fIEacEdc (float): 각각의 EDC
            fIDesEdc (float): 설계 EDC

        Returns:
            pass_fail (bool): 교량받침 3.5.3 품질기준 (1)의 판단 결과
        """
        assert isinstance(fIAveKef, float)
        assert isinstance(fIEacKef, float)
        assert isinstance(fIDesKef, float)
        assert isinstance(fIAveEdc, float)
        assert isinstance(fIEacEdc, float)
        assert isinstance(fIDesEdc, float)

        if fIAveKef > fIDesKef*0.9 and fIAveKef < fIDesKef*1.1:
            if fIEacKef > fIDesKef*0.8 and fIEacKef < fIDesKef*1.2:
                if fIAveEdc >= fIDesEdc*0.85:
                    if fIEacEdc >= fIDesEdc*0.75:
                        pass_fail = True
                    else:
                        pass_fail = False
                else:
                    pass_fail = False
            else:
                pass_fail = False
        else:
            pass_fail = False

        return RuleUnitResult(
            result_variables = {
                "pass_fail": pass_fail,
                })