import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS142010_020202_03(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = '서울대학교, 김정연'  # 작성자명
    ref_code = 'KCS 14 20 10 2.2.2 (3)' # 건설기준문서
    ref_date = '2023-10-04'  # 디지털 건설문서 작성일
    doc_date = '2022-09-01'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '일반콘크리트'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    일반콘크리트
    2. 자재
    2.2 배합
    2.2.2 배합강도
    (3)
    """

    # 건설기준문서내용(text)
    content = """
    #### 2.2.2 배합강도
    (3) 레디믹스트 콘크리트 사용자는 식 (2.2-2)에 따라 기온보정강도(T_{n})를 더하여 생산자에게 호칭강도(f_{cn})로 주문하여야 한다.

f_{cn} = f_{cq} + T_{n} (MPa)     (2.2-2)
여기서, ;기온보정강도 (MPa)로서 표 2.2-1에 따른다.

표 2.2-1 콘크리트 강도의 기온에 따른 보정값()

\begin{table}[]
\begin{tabular}{|
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l |
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l |}
\hline
\multicolumn{1}{|l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 결합재 종류}}                                                                                               & {\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}재령\\ (일)\end{tabular}} & \multicolumn{3}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 콘크리트 타설일로부터 재령까지의 예상평균기온의 범위(°C)}}                                                                                           \\ \hline
\multicolumn{1}{|l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}                                                                                                     & {\color[HTML]{333333} 28}                                               & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 18 이상}} & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 8 이상∼18 미만}} & {\color[HTML]{333333} 4 이상∼8 미만}  \\ \cline{2-5}
\multicolumn{1}{|l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}                                                                                                     & {\color[HTML]{333333} 42}                                               & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 12 이상}} & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 4 이상∼12 미만}} & {\color[HTML]{333333} -}          \\ \cline{2-5}
\multicolumn{1}{|l|}{\multirow{-3}{*}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}보통포틀랜드 시멘트\\ 플라이 애시 시멘트 1종\\ 고로 슬래그 시멘트 1종\end{tabular}}}} & {\color[HTML]{333333} 56}                                               & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 7 이상}}  & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 4 이상∼7 미만}}  & {\color[HTML]{333333} -}          \\ \hline
\multicolumn{1}{|l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}                                                                                                     & {\color[HTML]{333333} 28}                                               & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 18 이상}} & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 10이상∼18미만}}  & {\color[HTML]{333333} 4 이상∼10 미만} \\ \cline{2-5}
\multicolumn{1}{|l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}                                                                                                     & {\color[HTML]{333333} 42}                                               & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 13 이상}} & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 5 이상∼13 미만}} & {\color[HTML]{333333} 4 이상∼5 미만}  \\ \cline{2-5}
\multicolumn{1}{|l|}{\multirow{-3}{*}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 플라이 애시 시멘트 2종}}}                                                                      & {\color[HTML]{333333} 56}                                               & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 8 이상}}  & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 4 이상∼8 미만}}  & {\color[HTML]{333333} -}          \\ \hline
\multicolumn{1}{|l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}                                                                                                     & {\color[HTML]{333333} 28}                                               & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 18 이상}} & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 13이상∼18 미만}} & {\color[HTML]{333333} 4 이상∼13 미만} \\ \cline{2-5}
\multicolumn{1}{|l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}                                                                                                     & {\color[HTML]{333333} 42}                                               & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 14 이상}} & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 10이상∼14 미만}} & {\color[HTML]{333333} 4 이상∼10 미만} \\ \cline{2-5}
\multicolumn{1}{|l|}{\multirow{-3}{*}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 고로 슬래그 시멘트 2종}}}                                                                      & {\color[HTML]{333333} 56}                                               & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 10 이상}} & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 5 이상∼10 미만}} & {\color[HTML]{333333} 4 이상∼5 미만}  \\ \hline
\multicolumn{2}{|l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 콘크리트 강도의 기온에 따른 보정값 \# (MPa)}}                                                                                                                                                   & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 0}}     & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 3}}          & {\color[HTML]{333333} 6}          \\ \hline
\end{tabular}
\end{table}
    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A["Title: 레디믹스크 콘크리트 호칭강도"];
    B["KCS 14 31 30 2.2.2 (3)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 30 2.2.2 (3)"])

    subgraph Variable_def
    VarOut1[/"출력변수: 콘크리트 품질기준 강도"/];


		VarIn1[/"입력변수: 콘크리트 품질기준 강도"/];
		VarIn2[/"입력변수: 기온보정강도"/];
		VarIn3[/"입력변수: 결합재 종류"/];
		VarIn4[/"입력변수: 콘크리트 타설일로부터 재령까지의 예상평균기온의 범위(°C)"/];




    VarOut1  ~~~ VarIn1 & VarIn2 & VarIn3 & VarIn4
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{"결합재 종류, \n 콘크리트 타설일로부터 재령까지의 예상평균기온의 범위(°C)"}


		D -->|"표 2.2-1"|E["<img src='https://latex.codecogs.com/png.image?\dpi{110}T{n}'>-------"];
		E --> F["<img src='https://latex.codecogs.com/png.image?\dpi{110}f{cn}=f{cq}&plus;T{n}'>------------------------------------"];
		F --> G(["<img src='https://latex.codecogs.com/png.image?\dpi{110}T{n}'>-------"]);
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def ready_mixed_concrete_nominal_strength(fIFcq, fITn) :
        """레디믹스트 콘크리트 호칭강도

        Args:
            fIFcq (float): 콘크리트 품질기준 강도
            fITn (float): 기온보정강도

        Returns:
            fOFcn (float):레디믹스크 콘크리트 호칭강도

        """

        if fITn == 0:
            fOFcn = fIFcq + fITn
            return fOFcn

        if fITn == 3:
            fOFcn = fIFcq + fITn
            return fOFcn

        if fITn == 6:
            fOFcn = fIFcq + fITn
            return fOFcn