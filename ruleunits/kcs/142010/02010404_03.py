import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS142010_02010404_03(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = '서울대학교, 김정연'  # 작성자명
    ref_code = 'KCS 14 20 10 2.1.4.4 (3)' # 건설기준문서
    ref_date = '2023-10-04'  # 디지털 건설문서 작성일
    doc_date = '2022-09-01'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '일반콘크리트'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    일반콘크리트
    2. 자재
    2.1 구성재료
    2.1.4 굵은 골재
    2.1.4.4 유해물 함유량의 한도
    (3)
    """

    # 건설기준문서내용(text)
    content = """
    #### 2.1.4.4 유해물 함유량의 한도
   (3) 천연 굵은 골재의 점토덩어리 함유량은 0.25 %, 연한 석편은 5.0 % 이하이어야 하며, 그 합은 5 %를 초과하지 않아야 한다. 다만, 순환 굵은 골재의 점토덩어리 함유량은 0.2 % 이하로 한다. 그러나 무근콘크리트에 사용할 경우에는 적용하지 않는다.
    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A["Title: 천연 및 순환 굵은 골재의 유해물 함유량의 한도"];
    B["KCS 14 31 30 2.1.4.4 (3)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 30 2.1.4.4 (3)"])

    subgraph Variable_def
    VarOut1[/"출력변수: 유해물 함유량의 한도"/];

		VarIn1[/"입력변수: 무근콘크리트"/];
		VarIn2[/"입력변수: 천연 굵은 골재"/];
		VarIn3[/"입력변수: 순환 굵은 골재"/];
		VarIn4[/"입력변수: 점토덩어리 함유량"/];
		VarIn5[/"입력변수: 연한석편 함유량"/];



    VarOut1  ~~~ VarIn1 & VarIn2 & VarIn3 & VarIn4 & VarIn5
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{무근콘크리트}

		D --> |False|F{굵은 골재 종류}

		F --> |천연 굵은 골재|E{"점토덩어리 함유량 <= 0.25 %\n연한 석편 함유량 <= 5.0 %\n(점토덩어리+연한 석편) <= 5 %"}
		F --> |순환 굵은 골재|G{"점토덩어리 함유량 <= 0.2 %"}

		E --> |True|H([PASS])
		E --> |False|I([FAIL])


		G --> |True|H([PASS])
		G --> |False|I([FAIL])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def harmful_content_limit_in_natural_and_recycled_coarse_aggregates(bINonCon, bINatAgg, bIRecAgg, fIClaCon, fIRocCon) ->str :
        """천연 및 순환 굵은 골재의 유해물 함유량 한도

        Args:
            bINonCon (boolean): 무근콘크리트
            bINatAgg (boolean): 천연 굵은 골재
            bIRecAgg (boolean): 순환 굵은 골재
            fIClaCon (float): 점토덩어리 함유량
            fIRocCon (float): 연한석편 함유량


        Returns:
            sOLimJHar (string): 유해물 함유량의 한도

        """

        if bINonCon == False:
            if bINatAgg == True:
                if (fIClaCon <= 0.25) and (fIRocCon <= 5) and ((fIClaCon + fIRocCon) <= 5):
                    sOLimJHar = "PASS"
                    return sOLimJHar
                else:
                    sOLimJHar = "FAIL"
                    return sOLimJHar
            elif bIRecAgg == True:
                if fIClaCon <= 0.2:
                    sOLimJHar = "PASS"
                    return sOLimJHar
                else:
                    sOLimJHar = "FAIL"
                    return sOLimJHar