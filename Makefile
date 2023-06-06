# Included custom configs change the value of MAKEFILE_LIST
# Extract the required reference beforehand so we can use it for help target
MAKEFILE_NAME := $(word $(words $(MAKEFILE_LIST)),$(MAKEFILE_LIST))
# Include custom config if it is available
-include Makefile.config

# Application
PROJECT_NAME    := stac-dataloader
PROJECT_ROOT    := $(abspath $(lastword $(MAKEFILE_NAME))/..)
PROJECT_VERSION := 0.3.2

.DEFAULT_GOAL := help

## --- Informative targets --- ##

.PHONY: all
all: help

# Auto documented help targets & sections from comments
#	- detects lines marked by double octothorpe (#), then applies the corresponding target/section markup
#   - target comments must be defined after their dependencies (if any)
#	- section comments must have at least a double dash (-)
#
# 	Original Reference:
#		https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
# 	Formats:
#		https://misc.flogisoft.com/bash/tip_colors_and_formatting
_SECTION := \033[34m
_TARGET  := \033[36m
_NORMAL  := \033[0m
.PHONY: help
# note: use "\#\#" to escape results that would self-match in this target's search definition
help:	## print this help message (default)
	@echo "$(_SECTION)=== $(PROJECT_NAME) help ===$(_NORMAL)"
	@echo "Please use 'make <target>' where <target> is one of:"
#	@grep -E '^[a-zA-Z_-]+:.*?\#\# .*$$' $(MAKEFILE_LIST) \
#		| awk 'BEGIN {FS = ":.*?\#\# "}; {printf "    $(_TARGET)%-24s$(_NORMAL) %s\n", $$1, $$2}'
	@grep -E '\#\#.*$$' "$(PROJECT_ROOT)/$(MAKEFILE_NAME)" \
		| awk ' BEGIN {FS = "(:|\-\-\-)+.*?\#\# "}; \
			/\--/ {printf "$(_SECTION)%s$(_NORMAL)\n", $$1;} \
			/:/   {printf "    $(_TARGET)%-24s$(_NORMAL) %s\n", $$1, $$2} \
		'

.PHONY: version
version:	## display current version
	@-echo "$(PROJECT_NAME) version: $(PROJECT_VERSION)"

.PHONY: info
info:		## display make information
	@echo "Information about your make execution:"
	@echo "  PROJECT_NAME    $(PROJECT_NAME)"
	@echo "  PROJECT_ROOT    $(PROJECT_ROOT)"
	@echo "  PROJECT_VERSION $(PROJECT_VERSION)"

## --- Versioning targets --- ##

# Bumpversion 'dry' config
# if 'dry' is specified as target, any bumpversion call using 'BUMP_XARGS' will not apply changes
BUMP_XARGS ?= --verbose --allow-dirty
ifeq ($(filter dry, $(MAKECMDGOALS)), dry)
	BUMP_XARGS := $(BUMP_XARGS) --dry-run
endif

.PHONY: dry
dry: .bumpversion.cfg	## run 'bump' target without applying changes (dry-run)
ifeq ($(findstring bump, $(MAKECMDGOALS)),)
	$(error Target 'dry' must be combined with a 'bump' target)
endif

# pin bump2version to avoid issue with verbosity and dry-run reporting
.PHONY: bump
bump:	## bump version using VERSION specified as user input
	@-echo "Updating package version ..."
	@[ "${VERSION}" ] || ( echo ">> 'VERSION' is not set"; exit 1 )
	@which bump2version 1>/dev/null || pip install "bump2version<=0.5.10"
	@bump2version $(BUMP_XARGS) --new-version "${VERSION}" patch;

## --- Test operations --- ##

.PHONY: check
check:	## Validate linting, typings and
	@poetry run pre-commit

.PHONY: test
test:
	@pytest -vvv "$(PROJECT_ROOT)/tests"
