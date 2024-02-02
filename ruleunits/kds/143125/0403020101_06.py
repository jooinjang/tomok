import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143125_0403020101_06 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 14 31 25 4.3.2.1.1 (6)' # 건설기준문서
    ref_date = '2017-12-20'  # 고시일
    doc_date = '2023-12-04'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '폭비'    # 건설기준명

    #
    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.2 강관 간의 트러스접합
    4.3.2.1 원형강관
    4.3.2.1.1 적용한계
    (6)
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
		A[적용한계] ;
		B["KDS 14 31 25 4.3.2.1.1 (6)"] ;
		A ~~~ B
		end

		subgraph Variable_def
		VarIn1[/입력변수: 폭비/] ;
	  VarIn2[/입력변수: 원형 지강관의 외경/]
	  VarIn3[/입력변수: 바깥지름/]
		end


		Python_Class ~~~ Variable_def


    E{"접합형상"} ;
    D["<img src='https://latex.codecogs.com/svg.image?0.2<D_{b}/D\leq&space;1.0'>----------------------------------------------"] ;
    C["<img src='https://latex.codecogs.com/svg.image?0.4<D_{b}/D\leq&space;1.0'>----------------------------------------------"] ;
		Variable_def --> E
    E--T, Y, X, 겹침 K형 접합-->D
    E--간격 K형 접합-->C
		C & D --> Q(["PASS or Fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def width_ratio(fIbeta,fIDb,fID,fIuserdefined) -> bool:
        """폭비
        Args:
            fIbeta (float): 폭비
            fIDb (float): 원형 지강관의 외경
            fID (float): 바깥지름
            fIuserdefined (float): 사용자 선택

        Returns:
            bool: 강구조 연결 설계기준(하중저항계수설계법) 4.3.2.1.1 적용한계 (6)의 통과여부
        """

        # T, Y, K형 이음의 경우 : fIuserdefined == 1
        # X형 접합의 경우 : fIuserdefined == 2

        fIbeta = fIDb / fID
        if fIuserdefined == 1:
            if 0.2 < fIbeta <= 1.0:
              return "Pass"
            else:
              return "Fail"
        elif fIuserdefined == 2:
            if 0.4 < fIbeta <= 1.0:
              return "Pass"
            else:
              return "Fail"


# 

