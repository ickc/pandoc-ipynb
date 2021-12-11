pandoc = pandoc

IPYNB = $(wildcard *.ipynb)
NBCONVERTED = $(patsubst %.ipynb,%.html,$(IPYNB))
PANDOCCONVERTED = $(patsubst %.ipynb,%-pandoc.html,$(IPYNB))

all: $(NBCONVERTED) $(PANDOCCONVERTED)

%.html: %.ipynb
	jupyter-nbconvert $< --to html

# $(pandoc) -s -o $@ $< -V header-includes='<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.6/require.min.js"></script>' --self-contained
%-pandoc.html: %.ipynb
	$(pandoc) -s -o $@ $< -V header-includes='<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.6/require.min.js"></script>' --extract-media=media
%.native: %.ipynb
	$(pandoc) -s -o $@ $<
print-%:
	$(info $* = $($*))

format:
	find -name '*.ipynb' -exec jupytext --sync --pipe black --pipe 'isort - --treat-comment-as-code "# %%" --float-to-top' {} +
