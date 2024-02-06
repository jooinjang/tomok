import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_01050202_05 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 24 14 21 1.5.2.2 (5)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-10-19'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '받침점의 계수 휨 모멘트'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    1. 일반사항
    1.5 구조해석
    1.5.2 구조물의 이상화
    1.5.2.2 기하학적 자료
    (5)
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
    A[계수 휨 모멘트];
    B["KDS 24 14 21 1.5.2.2 (5)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 계수 휨모멘트/];
    VarIn2[/입력변수: 계수 휨모멘트 변화량/] ;
    VarIn3[/입력변수: 받침점의 계수 반력/];
		VarIn4[/입력변수: 받침점 폭/];

		end
		Python_Class ~~~ Variable_def;
		Variable_def-->C
		C["<img src='https://latex.codecogs.com/svg.image?\Delta&space;M_{U}=f_{u,sup}t/8'>--------------------------------------------------------"];
		D(["계수 휨모멘트"]);

    C--->D
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Modulus_Bending_Moment(fImodbem,fIdeltaMu,fIfusup,fIt) -> float:
        """받침점의 계수 휨 모멘트

        Args:
            fImodbem (float) : 계수 휨모멘트
            fIdeltaMu (float) : 계수 휨모멘트 변화량
            fIfusup (float) : 받침점의 계수 반력
            fIt (float) : 받침점 폭




        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 1.5.2.2 기하학적 자료 (5)의 값
        """

        fIdeltaMu = fIfusup*fIt/8
        return fImodbem-fIdeltaMu


# 
