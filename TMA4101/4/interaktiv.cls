\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{interaktiv}[2016/05/30 - Klassefil for interaktive forelesninger] 
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
\ProcessOptions
\LoadClass{article}
\RequirePackage{amsmath}
\RequirePackage{amssymb}
\RequirePackage{babel}
\RequirePackage{etoolbox}
\RequirePackage{fancyhdr}
\advance\textwidth8pc
\advance\oddsidemargin-3pc
\advance\evensidemargin-3pc
\advance\textheight6\baselineskip
\advance\topmargin-3\baselineskip

%
% En oppgave kan plasseres mellom \begin{oppgave}{nummer} og
% \end{oppgave}
%

\newenvironment{oppgave}[1]{%
   \addvspace\medskipamount
   \begin{list}%
     {\fbox{\large {#1}}}%
     {\topsep\z@}
   \item}%
   {\end{list}}

%
% Bruk \bPunkt og \ePunkt for a), b), etc.
%

\newcounter{Punkt}
\newcommand{\bPunkt}{\stepcounter{Punkt}%
	\begin{list}{\textbf{\alph{Punkt})}}{} \item}
	\newcommand{\ePunkt}{\end{list}}

%
% Egen overskriftsstil
%

{\escapechar=-1
 \let~\expandafter
  \def\do#1{\xdef#1{\gdef~\noexpand\csname @\string#1\endcsname}}
 \do\emnekode
 \do\emnenavn
}

\renewcommand{\maketitle}{
  \centerline{\Large \@title} \vskip 27pt
  \centerline{\@author} \vskip 16pt
}

\patchcmd{\@settitle}{\uppercasenonmath\@title}{}{}{}
\patchcmd{\@setauthors}{\MakeUppercase}{}{}{}
\patchcmd{\section}{\scshape}{}{}{}

\pagestyle{fancy}
\lhead{}
\chead{\@emnekode ~ \@emnenavn}
\rhead{}
\cfoot{\thepage}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}

\fancypagestyle{plain}{%
  \renewcommand{\headrulewidth}{0pt}%
  \fancyfoot{}
}
  