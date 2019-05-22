pandoc = pandoc

IPYNB = $(wildcard *.ipynb)
NBCONVERTED = $(patsubst %.ipynb,%.html,$(IPYNB))
PANDOCCONVERTED = $(patsubst %.ipynb,%-pandoc.html,$(IPYNB))

all: $(NBCONVERTED) $(PANDOCCONVERTED)

%.html: %.ipynb
	jupyter-nbconvert $<
%-pandoc.html: %.ipynb
	# pandoc --ipynb-output=all --extract-media=media -s -o $@ $< # run forever
	$(pandoc) -s -o $@ $<

print-%:
	$(info $* = $($*))
