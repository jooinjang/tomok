import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS115015_04010108_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seonghan Yoon'  # 작성자명
    ref_code = 'KDS 11 50 15 4.1.1.8 (1)' # 건설기준문서
    ref_date = '2021-05-12'  # 디지털 건설문서 작성일
    doc_date = '2023-09-15'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '말뚝의 축방향 허용인발저항력'    # 건설기준명

    #
    description = """
    깊은기초 설계기준(일반설계법)
    4. 설계
    4.1 말뚝기초
    4.1.1 말뚝의 축방향 지지력과 변위
    4.1.1.8 말뚝의 축방향 허용인발저항력
    (1)
    """
    # https://dillinger.io/ 표와 이미지 랜더링 확인 사이트
    # 이미지 링크 변환 사이트 https://www.somanet.xyz/2017/06/blog-post_21.html
    # 건설기준문서내용(text)
    content = """
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[외말뚝의 허용인발저항력];
    B["KDS 11 50 15 4.1.1.8 (1)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarOut[/출력변수: 외말뚝의 허용인발저항력/];
    VarIn1[/입력변수: 인발시험 축방향 허용인발저항력/] ;
    VarIn2[/입력변수: 말뚝의 무게/];
    VarIn3[/입력변수: 말뚝본체의 허용인발하중/];

		VarOut~~~VarIn1
		VarOut~~~VarIn2
		VarOut~~~VarIn3
		end
		Python_Class ~~~ Variable_def;

		C["외말뚝의 허용인발저항력=\n min(인발시험 축방향허용인발저항력+말뚝의 무게, 말뚝본체의 허용인발하중)"]


    Variable_def--->C
    C---->D
    D(["외말뚝의 허용인발저항력"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def allowable_pull_out_resistance_of_external_pile(fOaporep,fIapores,fIwepile,fIapolpb) -> float:
        """말뚝의 축방향 허용인발저항력

        Args:
            fOaporep (float): 외말뚝의 허용인발저항력
            fIapores (float): 축방향 허용인발저항력
            fIwepile (float): 말뚝의 무게
            fIapolpb (float): 말뚝본체의 허용인발하중

        Returns:
            float: 깊은기초 설계기준(일반설계법)  4.1.1.8 말뚝의 축방향 허용인발저항력 (1)의 값
        """

        fOaporep = min(fIapores+fIwepile,fIapolpb)
        return fOaporep


# 
