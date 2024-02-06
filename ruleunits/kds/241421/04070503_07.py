import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04070503_07 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanhyuk Kim'  # 작성자명
    ref_code = 'KDS 24 14 21 4.7.5.3 (7)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-20'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '프리캐스트 콘크리트 휨부재 사이의 종방향 시공이음의 키'  # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.7 구조 형식에 따른 추가 규정
    4.7.5 슬래브교
    4.7.5.3 프리캐스트 슬래브교
    (7)
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
    A["프리캐스트 슬래브교"];
    B["KDS 24 14 21 4.7.5.3 (7)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수:압축 강도를 갖는 무수축 모르터/];
		VarIn2[/입력변수:키의 깊이/];

		VarIn1 & VarIn2

		end
		Python_Class ~~~ Variable_def
		Variable_def--->D--->E

		D["압축 강도를 갖는 무수축 모르터=35MPa"]
		E["165mm≤키의 깊이"]
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Shrink_free_mortar_with_compressive_strength (fIshmcst, fIkeydep) ->bool:
        """프리캐스트 콘크리트 휨부재 사이의 종방향 시공이음의 키
        Args:
             fIshmcst (float): 압축 강도를 갖는 무수축 모르터
             fIkeydep (float): 키의 깊이
        Returns:
            bool: 콘크리트교 설계기준 (한계상태설계법) 4.7.5.3 (7) 설계기준에 따른 프리캐스트 콘크리트 휨부재 사이의 종방향 시공이음의 키 적합여부
        """
        if fIshmcst==35 and fIkeydep >= 165:
          return "Pass"
        else:
          return "Fail"


# 
