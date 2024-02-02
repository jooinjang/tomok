import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_0405040206 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 14 31 10 4.5.4.2.6' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-12-13'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '이음부 공칭강도'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.5. 기타 부재
    4.5.4 파형강판 구조물
    4.5.4.2 아치형 파형강판 구조물
    4.5.4.2.6 이음부 강도
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
		A[Title: 이음부 강도] ;
		B["KDS 14 31 10 4.5.4.2.6"] ;
		A ~~~ B
		end

      subgraph Variable_def
      VarIn1[/입력변수: 이음부 공칭강도/] ;
      VarIn2[/입력변수: 이음부 저항계수/] ;
      VarIn3[/입력변수: 설계압축력/] ;
		end

		Python_Class ~~~ Variable_def

		Q["<img src=https://latex.codecogs.com/svg.image?T_{f}<\phi&space;_{j}S_{s}>---------------------"]

		Variable_def --> Q --> X(["PASS or Fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Nominal_joint_strength(fISs,fIphij,fITf) -> bool:
        """이음부 공칭강도
        Args:
            fISs (float): 이음부 공칭강도
            fIphij (float): 이음부 저항계수
            fITf (float): 설계압축력


        Returns:
            bool: 강구조부재설계기준(하중저항계수설계법)  4.5.4.2.6 이음부 강도의 통과여부
        """


        if fITf < fIphij * fISs:
          return "Pass"
        else:
          return "Fail"


# 

