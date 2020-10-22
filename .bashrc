#
# ~/.bashrc
#

#Export paths and variables
export TERM="alacritty"

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

#Optimized aliases

alias grep='grep --color=auto'
alias ls='ls --color=auto --group-directories-first'
alias ll='ls -la'
alias vim='nvim'

#Change title of the terminals
case ${TERM} in
	xterm*|rxvt*|Eterm*|aterm|kterm|gnome*|alacritty|st|konsole*)
		PROMPT_COMMAND='echo -ne "\033]0;${TERM^} ${PWD/#$HOME/\~}\007"'
		;;
esac

#Extract compressed files
# usage: ex <file>
ex()
{
	if [ -f $1 ] ; then
		echo "Extracting file '$1'"
		case $1 in
			*.tar.bz2)	tar xjf $1	;;
			*.tar.gz)	tar xzf $1	;;
			*.bz2)		bunzip2 $1	;;
			*.rar)		unrar x $1	;;
			*.gz)		gunzip $1	;;
			*.tar)		tar xf $1	;;
			*.tbz2)		tar xjf $1	;;
			*.tgz)		tar xzf $1	;;
			*.zip)		unzip $1	;;
			*.Z)		uncompress $1	;;
			*.7z) 		7z x $1		;;
			*.deb)		ar x $1		;;
			*.tar.xz)	tar xf $1	;;
			*.tar.zst)	unzstd $1	;;
			*)		echo "'$1' cannot be extracted via ex()";;
		esac
	else
		echo "'$1' not a valid file"
	fi
}


PS1='[\u@\h \W]\$ '
