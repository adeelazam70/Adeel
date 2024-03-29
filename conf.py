# -*- coding: utf-8 -*-
#
# sellor documentation build configuration file, created by
# sphinx-quickstart on Tue Jan  5 11:54:57 2016.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os
import shlex

#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = ''
copyright = '2019,'
author = 'Aqeel Chishti'

# The short X.Y version.
version = u'1.0.2'
# The full version, including alpha/beta/rc tags.
release = ''
#release = 'Online Shop'

# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

exclude_patterns = ['_build']

#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = ''

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = 'logo.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr'
#html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# Now only 'ja' uses this config value
#html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
#html_search_scorer = 'scorer.js'
#numfig = True
# Output file base name for HTML help builder.
htmlhelp_basename = 'sellordoc'

numfig_format = {'figure': 'Figure %s',
                 'table': 'Table %s'
                }
numfig = True
#numfig_format = {'figure': 'Fig. %s'}

latex_engine = 'pdflatex'
latex_elements = {
    'papersize': 'a4paper',
    'releasename':" ",
    #'releasename': '',
    # Sonny, Lenny, Glenn, Conny, Rejne, Bjarne and Bjornstrup
    'fncychap': '\\usepackage[]{fncychap}',
    'fontspec': '\\usepackage{Times New Roman}',
    'fontpkg': '\\usepackage{times}',
    'geometry': '\\usepackage[vmargin=3cm, hmargin=2.6cm]{geometry}',

    'figure_align': 'htpb!',
    # The font size ('10pt', '11pt' or '12pt').
    #
    'pointsize': '12pt',

    # Additional stuff for the LaTeX preamble.
    #
    'preamble': r'''
        %\setmainfont{Times New Roman}
        %\usepackage{cleanthesis}
        \usepackage{fancyhdr}
        \usepackage[utf8]{inputenc}
        \pagestyle{empty}
        \usepackage{mathptmx}
        \usepackage[T1]{fontenc} 
        \fancyhf{}
        
        \renewcommand\headrule{}
        \renewcommand\footrule{}
        
        \usepackage{float}
        \usepackage{xcolor}
        \usepackage{hyperref}
        \hypersetup{colorlinks=true, linkcolor=red}
        
        \setlength{\parindent}{3em}
        \setlength{\parskip}{1em}
        \renewcommand{\baselinestretch}{1.3}
       
        \usepackage{graphicx}
        \usepackage{times,amsmath,amsfonts,amssymb,amsthm}
        
        \usepackage{float}
        \usepackage[export]{adjustbox}
        
        \usepackage{titlesec}
        \titleformat{\chapter}[display]{\LARGE\bfseries\centering}{\chaptertitlename\ 
        \thechapter}{0pt}{\Huge}
        \titleformat{\section}{\Large\bfseries}{\thesection}{1.2em}{}
        \titleformat{\subsection}{\large\bfseries}{\thesubsection}{0.8em}{}
        \titleformat{\subsubsection}{\normalsize\bfseries}{\thesubsubsection}{0.6em}{}
        \titlespacing*{\chapter}{0pt}{30pt}{20pt}

        %%% Alternating Header for oneside
        
        \fancyhead[L]{\ifthenelse{\isodd{\value{page}}}{\tiny\nouppercase{\leftmark}}}
        \fancyhead[R]{\ifthenelse{\isodd{\value{page}}}{\tiny\nouppercase{\rightmark}}}
        
        %% for oneside: change footer at right side. If you want to use Left and right then use same as header defined above.
        \fancyfoot[R]{\ifthenelse{\isodd{\value{page}}}{\tiny}}

        %%% page number
        \fancyfoot[CO, CE]{\thepage}
        
        \RequirePackage{tocbibind} %%% comment this to remove page number for following
        \addto\captionsenglish{\renewcommand{\contentsname}{Table of contents}}
        %\addto\captionsenglish{\renewcommand{\chaptername}{Chapter}}{\centering}
    ''',


    'maketitle': r'''
        \pagenumbering{Roman} %%% to avoid page 1 conflict with actual page 1

        \begin{titlepage}
            \centering

            \vspace*{40mm} %%% * is used to give space from top
           \textbf{\Huge {SELLOR DOCUMANTATION}}

            \vspace{0mm}
            \textbf{{A modular, high performance e-commerce storefront built with Python & Django}}
            
            \vspace*{0mm}
        \end{titlepage}
        
        \clearpage
        \pagenumbering{roman}
        \hypersetup{linkcolor=black}
        \tableofcontents
        \listoffigures
        \listoftables
        \clearpage
        \References
        \pagenumbering{arabic}
        ''',
    # Latex figure (float) alignment
    #
    
    'tableofcontents':' ',
}

latex_documents = [
   (master_doc, 'sellor.tex', ' ',
     'Aqeel Chishti', 'report')
]




# -- Options for LaTeX output ---------------------------------------------
#    latex_engine = 'pdflatex'
#    latex_elements = {
    
# The paper size ('letterpaper' or 'a4paper').
#    'papersize': 'a4paper',

# The font size ('10pt', '11pt' or '12pt').
#    'pointsize': '12pt',
    
#    'fontpkg': '\\usepackage{times}',
#    'geometry': '\\usepackage[vmargin=2.5cm, hmargin=2.5cm]{geometry}',
#    'fncychap': '\\usepackage[Conny]{fncychap}',
     
#    'preamble': r'''
    #%%% Alternating Header for oneside
    #\fancyhead[L]{\ifthenelse{\isodd{\value{page}}}{ \small \nouppercase{\leftmark} }{}}
    #\fancyhead[R]{\ifthenelse{\isodd{\value{page}}}{}{ \small \nouppercase{\rightmark} }}
    
    #%% for oneside: change footer at right side. If you want to use Left and right then use same as header defined above.
    #\fancyfoot[R]{\ifthenelse{\isodd{\value{page}}}{{\tiny Meher Krishna Patel} }{\href{http://pythondsp.readthedocs.io/en/latest/pythondsp/toc.html}{\tiny PythonDSP}}}
#''',
#'printindex': '\\footnotesize\\raggedright\\printindex',

# Additional stuff for the LaTeX preamble.
#'preamble': '',

# Latex figure (float) alignment
#'figure_align': 'htbp',
#}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
#latex_documents = [
# (master_doc, 'sellor.tex', u'Sellor Documentation',
#   u'Sellor', 'manual'),
#]


# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = True

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, '', u'',
     [author], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  (master_doc, 'Ecommerce Website for Online Shopping', u'',
   author, 'Aqeel Chishti', '.',
   ''),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False

