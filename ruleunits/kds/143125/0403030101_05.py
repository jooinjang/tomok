import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143125_0403030101_05 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jonghyeok Lee'  # 작성자명
    ref_code = 'KDS 14 31 25 4.3.3.1.1 (5)' # 건설기준문서
    ref_date = '2017-12-20'  # 고시일
    doc_date = '2023-12-05'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '폭비'  # 건설기준명


    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.3 강관 간의 모멘트접합
    4.3.3.1 원형강관
    4.3.3.1.1 적용한계
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
        A[Title: 적용한계] ;
        B["KDS 14 31 25 4.3.3.1.1(5)"] ;
        A ~~~ B
        end

        subgraph Variable_def
        VarOut1[/출력변수: 폭비/] ;
        VarIn1[/입력변수: 원형 지강관의 외경/] ;
        VarIn2[/입력변수: 바깥지름/] ;
        VarOut1 ~~~ VarIn1 & VarIn2
        end

        Python_Class ~~~ Variable_def
        D(["폭비"]) ;
        E["<img src='https://latex.codecogs.com/svg.image?0.2<D_{b}/D\leq&space;1.0'>-----------------------------------------"] ;
        Variable_def -->E-->D
        """

      # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def width(fOwidth,fIDb,fID) -> bool:
        """폭비

        Args:
            fOwidth (float): 폭비
            fIDb (float): 원형 지강관의 외경
            fID (float): 바깥지름

        Returns:
            bool : 강구조 연결 설계기준(하중저항계수설계법)  4.3.3.1.1 적용한계 (5) 의 통과여부
        """

        if 0.2 < fIDb/fID <= 1.0:
          return("Pass")
        else:
          return("Fail")


# 
