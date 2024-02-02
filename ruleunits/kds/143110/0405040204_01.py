import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_0405040204_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 14 31 10 4.5.4.2.4 (1)' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-12-15'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '파형강판 구조물의 압축좌굴'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.5 기타 부재
    4.5.4 파형강판 구조물
    4.5.4.2 아치형 파형강판 구조물
    4.5.4.2.4 압축좌굴
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
		A[Title: 압축좌굴] ;
		B["KDS 14 31 10 4.5.4.2.4 (1)"] ;
		A ~~~ B
		end

      subgraph Variable_def
      VarIn1[/입력변수: 설계압축응력/] ;
      VarIn2[/입력변수: 설계압축력/] ;
      VarIn3[/입력변수: 파형강판의 단면적/] ;
      VarIn4[/입력변수: 설계좌굴강도/] ;
			end

		VarIn1 & VarIn2 ~~~ VarIn3 & VarIn4

		Python_Class ~~~ Variable_def

		Q["<img src=https://latex.codecogs.com/svg.image?f_{c}=\frac{T_{f}}{A}\leq&space;f_{b}>--------------------------------------"]

		Variable_def --> Q --> D(["PASS or Fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Design_compressive_stress(fIfc,fITf,fIA,fIfb) -> bool:
        """파형강판 구조물의 압축좌굴
        Args:
            fIfc (float): 설계압축응력
            fITf (float): 설계압축력
            fIA (float): 파형강판의 단면적
            fIfb (float): 설계좌굴강도


        Returns:
            bool: 강구조부재설계기준(하중저항계수설계법)  4.5.4.2.4 압축좌굴 (1)의 통과여부
        """

        fIfc = fITf / fIA
        if fITf / fIA <= fIfb:
          return "Pass"
        else:
          return "Fail"


# 

