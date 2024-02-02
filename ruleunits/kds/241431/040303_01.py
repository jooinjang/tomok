import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241431_040303_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 24 14 31 4.3.3 (1)' # 건설기준문서
    ref_date = '2018-08-30'  # 고시일
    doc_date = '2023-09-04'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '강재의 최소두께'    # 건설기준명

    #
    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.3 부재에 관한 일반사항
    4.3.3 강재의 최소두께
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
		A[강재의 최소두께];
		B["KDS 24 14 31 4.3.3.1"];
		A ~~~ B
		end

	  subgraph Variable_def
		VarIn1[/입력변수: 강재의 최소두께/] ;
		end

    Python_Class ~~~ Variable_def
       Variable_def -->D
    D["강재의 최소두께 &ge; 8mm"];
    D --> H([PASS or Fail]);
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Steel_minimum_thickness(fIstmith) -> bool:
        """강재의 최소두께

        Args:
            fIstmith (float): 강재의 최소두께

        Returns:
            bool: 강교 설계기준(한계상태설계법)  4.3.3 강재의 최소두께 (1)의 통과 여부
        """

        if fIstmith >= 8 :
          return "Pass"
        else:
          return "Fail"


# 

