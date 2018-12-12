def star(charliebrownskiteeatingtree, flakesize, flakecolour):
    charliebrownskiteeatingtree.color('black', flakecolour)
    charliebrownskiteeatingtree.begin_fill()
    for i in range(12):
        charliebrownskiteeatingtree.forward(flakesize)
        charliebrownskiteeatingtree.left(150)
    charliebrownskiteeatingtree.end_fill()
