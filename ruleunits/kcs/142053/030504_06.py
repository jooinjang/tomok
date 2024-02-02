import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS142053_030504_06(RuleUnit):

    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 14 20 53 3.5.4 (6)'
    ref_date = '2022-01-11'
    doc_date = '2023-09-21'
    title = '텐던의 신장량 관리'

    # 건설기준문서항목 (분류체계정보)
    description = """
    프리스트레스트 콘크리트
    3. 시공
    3.5 프리스트레싱
    3.5.4 프리스트레싱의 관리
    (6)
    """

    # 건설기준문서내용(text)
    content = """
    ####(6) 텐던의 신장량을 관리할 때 포스트텐션 시공 현장에서 확인된 마찰계수와 탄성계수 등을 반영한 이론적인 계산값과 측정값의 차이는 15 m 이하의
    짧은 텐던의 경우 각각의 텐던에 대해서 ±15 %, 전체 텐던에 대해서 ±7 %를 넘지 않아야 하며, 15 m 이상의 긴 텐던의 경우 각각의 텐던에 대해서
    ±10 %, 전체 텐던에 대해서 ±5 %를 넘지 않아야 한다. 단, 비부착 단일 강연선 텐던의 경우 길이와 상관없이 각각의 텐던에 대해서 ±7 %를 넘지 않
    아야 한다. 한편 프리텐션 시공의 경우에는 길이와 상관없이 각각의 강연선에 대해서 계산값과 측정값의 차이가 ±5 %를 넘지 않아야 한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 텐던의 신장량 관리];
    B["KCS 14 20 53 3.5.4 (6)"];
    B ~~~ A
    end

    KCS(["KCS 14 20 53 3.5.4 (6)"])

    subgraph Variable_def
    VarOut[/출력변수: 텐던의 신장량 관리/];
    VarIn1[/입력변수: 포스트텐션 시공/];
    VarIn2[/입력변수: 텐던의 길이/];
    VarIn3[/입력변수: 전체 텐던의 길이/];
    VarIn4[/입력변수: 각 텐던 신장량의 이론값/];
    VarIn5[/입력변수: 각 텐던 신장량의 측정값/];
    VarIn6[/입력변수: 전체 텐던 신장량의 이론값/];
    VarIn7[/입력변수: 전체 텐던 신장량의 측정값/];
    VarIn8[/입력변수: 비부착 단일 강연선 텐던/];
    VarIn9[/입력변수: 프리텐션 시공/];
    VarOut ~~~ VarIn1 & VarIn2 & VarIn3 & VarIn4 & VarIn5
    VarIn3 ~~~ VarIn6 & VarIn7 & VarIn8 & VarIn3
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"포스트텐션 시공 \n 비부착 단일 강연선 텐던 \n 프리텐션 시공"}
    C --> |포스트텐션 시공|D{텐던의 길이}
    D --> |"텐던의 길이 ≤ 15 m"|E{"|각 텐던 신장량의 이론값-각 텐던 신장량의 측정값| \n < 텐던의 길이*0.15 \n & \n |전체 텐던 신장량의 이론값-전체 텐던 신장량의 측정값| \n < 전체 텐던의 길이*0.07 \n."}
    D --> |"텐던의 길이 > 15 m"|F{"|각 텐던 신장량의 이론값-각 텐던 신장량의 측정값| \n < 텐던의 길이*0.10 \n & \n |전체 텐던 신장량의 이론값-전체 텐던 신장량의 측정값| \n < 전체 텐던의 길이*0.05 \n."}
    C --> |비부착 단일 강연선 텐던|G{"|각 텐던 신장량의 이론값-각 텐던 신장량의 측정값| \n < 텐던의 길이*0.07"}
    C --> |프리텐션 시공|H{"|각 텐던 신장량의 이론값-각 텐던 신장량의 측정값| \n < 텐던의 길이*0.05"}
    E & F & G & H --> |True|Pass([Pass])
    E & F & G & H --> |False|Fail([Fail])
    """

    @rule_method
    def tendon_elongation(bIPosCon,fITenLen_1, fITenLen_2, fITheTen_1,fIMeaTen_1, fITheTen_2 , fIMeaTen_2, bIUnbStr,bIPreCon ) -> str:
        """
        Args:
            bIPosCon (boolean): 포스트텐션 시공
            fITenLen_1 (float): 텐던의 길이
            fITenLen_2 (float): 전체 텐던의 길이
            fITheTen_1 (float): 각 텐던 신장량의 이론값
            fIMeaTen_1 (float): 각 텐던 신장량의 측정값
            fITheTen_2 (float): 전체 텐던 신장량의 이론값
            fIMeaTen_2 (float): 전체 텐던 신장량의 측정값
            bIUnbStr (boolean): 비부착 단일 강연선 텐던
            bIPreCon (boolean): 프리텐션 시공
        Returns:
            sOManTen (string): 텐던의 신장량 관리
        """
        if bIPosCon:
            if fITenLen_1 <= 15:
                if abs(fITheTen_1-fIMeaTen_1) < fITenLen_1*0.15 and abs(fITheTen_2-fIMeaTen_2) < fITenLen_2*0.07:
                    sOManTen = "Pass"
                else:
                    sOManTen = "Fail"
            else:
                if abs(fITheTen_1-fIMeaTen_1) < fITenLen_1*0.1 and abs(fITheTen_2-fIMeaTen_2) < fITenLen_2*0.05:
                    sOManTen = "Pass"
                else:
                    sOManTen = "Fail"
        elif bIUnbStr:
            if abs(fITheTen_1-fIMeaTen_1) < fITenLen_1*0.07:
                sOManTen = "Pass"
            else:
                sOManTen = "Fail"
        elif bIPreCon:
            if abs(fITheTen_1-fIMeaTen_1) < fITenLen_1*0.05:
                sOManTen = "Pass"
            else:
                sOManTen = "Fail"
        return sOManTen