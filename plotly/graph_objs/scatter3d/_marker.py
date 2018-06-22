from plotly.basedatatypes import BaseTraceHierarchyType


class Marker(BaseTraceHierarchyType):

    # autocolorscale
    # --------------
    @property
    def autocolorscale(self):
        """
        Has an effect only if `marker.color` is set to a numerical
        array. Determines whether the colorscale is a default palette
        (`autocolorscale: true`) or the palette determined by
        `marker.colorscale`. In case `colorscale` is unspecified or
        `autocolorscale` is true, the default  palette will be chosen
        according to whether numbers in the `color` array are all
        positive, all negative or mixed.
    
        The 'autocolorscale' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['autocolorscale']

    @autocolorscale.setter
    def autocolorscale(self, val):
        self['autocolorscale'] = val

    # cauto
    # -----
    @property
    def cauto(self):
        """
        Has an effect only if `marker.color` is set to a numerical
        array and `cmin`, `cmax` are set by the user. In this case, it
        controls whether the range of colors in `colorscale` is mapped
        to the range of values in the `color` array (`cauto: true`), or
        the `cmin`/`cmax` values (`cauto: false`). Defaults to `false`
        when `cmin`, `cmax` are set by the user.
    
        The 'cauto' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['cauto']

    @cauto.setter
    def cauto(self, val):
        self['cauto'] = val

    # cmax
    # ----
    @property
    def cmax(self):
        """
        Has an effect only if `marker.color` is set to a numerical
        array. Sets the upper bound of the color domain. Value should
        be associated to the `marker.color` array index, and if set,
        `marker.cmin` must be set as well.
    
        The 'cmax' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['cmax']

    @cmax.setter
    def cmax(self, val):
        self['cmax'] = val

    # cmin
    # ----
    @property
    def cmin(self):
        """
        Has an effect only if `marker.color` is set to a numerical
        array. Sets the lower bound of the color domain. Value should
        be associated to the `marker.color` array index, and if set,
        `marker.cmax` must be set as well.
    
        The 'cmin' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['cmin']

    @cmin.setter
    def cmin(self, val):
        self['cmin'] = val

    # color
    # -----
    @property
    def color(self):
        """
        Sets the marker color. It accepts either a specific color or an
        array of numbers that are mapped to the colorscale relative to
        the max and min values of the array or relative to `cmin` and
        `cmax` if set.
    
        The 'color' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color:
                aliceblue, antiquewhite, aqua, aquamarine, azure,
                beige, bisque, black, blanchedalmond, blue,
                blueviolet, brown, burlywood, cadetblue,
                chartreuse, chocolate, coral, cornflowerblue,
                cornsilk, crimson, cyan, darkblue, darkcyan,
                darkgoldenrod, darkgray, darkgrey, darkgreen,
                darkkhaki, darkmagenta, darkolivegreen, darkorange,
                darkorchid, darkred, darksalmon, darkseagreen,
                darkslateblue, darkslategray, darkslategrey,
                darkturquoise, darkviolet, deeppink, deepskyblue,
                dimgray, dimgrey, dodgerblue, firebrick,
                floralwhite, forestgreen, fuchsia, gainsboro,
                ghostwhite, gold, goldenrod, gray, grey, green,
                greenyellow, honeydew, hotpink, indianred, indigo,
                ivory, khaki, lavender, lavenderblush, lawngreen,
                lemonchiffon, lightblue, lightcoral, lightcyan,
                lightgoldenrodyellow, lightgray, lightgrey,
                lightgreen, lightpink, lightsalmon, lightseagreen,
                lightskyblue, lightslategray, lightslategrey,
                lightsteelblue, lightyellow, lime, limegreen,
                linen, magenta, maroon, mediumaquamarine,
                mediumblue, mediumorchid, mediumpurple,
                mediumseagreen, mediumslateblue, mediumspringgreen,
                mediumturquoise, mediumvioletred, midnightblue,
                mintcream, mistyrose, moccasin, navajowhite, navy,
                oldlace, olive, olivedrab, orange, orangered,
                orchid, palegoldenrod, palegreen, paleturquoise,
                palevioletred, papayawhip, peachpuff, peru, pink,
                plum, powderblue, purple, red, rosybrown,
                royalblue, saddlebrown, salmon, sandybrown,
                seagreen, seashell, sienna, silver, skyblue,
                slateblue, slategray, slategrey, snow, springgreen,
                steelblue, tan, teal, thistle, tomato, turquoise,
                violet, wheat, white, whitesmoke, yellow,
                yellowgreen
          - A number that will be interpreted as a color
            according to scatter3d.marker.colorscale
          - A list or array of any of the above

        Returns
        -------
        str|numpy.ndarray
        """
        return self['color']

    @color.setter
    def color(self, val):
        self['color'] = val

    # colorbar
    # --------
    @property
    def colorbar(self):
        """
        The 'colorbar' property is an instance of ColorBar
        that may be specified as:
          - An instance of plotly.graph_objs.scatter3d.marker.ColorBar
          - A dict of string/value properties that will be passed
            to the ColorBar constructor
    
            Supported dict properties:
                
                bgcolor
                    Sets the color of padded area.
                bordercolor
                    Sets the axis line color.
                borderwidth
                    Sets the width (in px) or the border enclosing
                    this color bar.
                dtick
                    Sets the step in-between ticks on this axis.
                    Use with `tick0`. Must be a positive number, or
                    special strings available to *log* and *date*
                    axes. If the axis `type` is *log*, then ticks
                    are set every 10^(n*dtick) where n is the tick
                    number. For example, to set a tick mark at 1,
                    10, 100, 1000, ... set dtick to 1. To set tick
                    marks at 1, 100, 10000, ... set dtick to 2. To
                    set tick marks at 1, 5, 25, 125, 625, 3125, ...
                    set dtick to log_10(5), or 0.69897000433. *log*
                    has several special values; *L<f>*, where `f`
                    is a positive number, gives ticks linearly
                    spaced in value (but not position). For example
                    `tick0` = 0.1, `dtick` = *L0.5* will put ticks
                    at 0.1, 0.6, 1.1, 1.6 etc. To show powers of 10
                    plus small digits between, use *D1* (all
                    digits) or *D2* (only 2 and 5). `tick0` is
                    ignored for *D1* and *D2*. If the axis `type`
                    is *date*, then you must convert the time to
                    milliseconds. For example, to set the interval
                    between ticks to one day, set `dtick` to
                    86400000.0. *date* also has special values
                    *M<n>* gives ticks spaced by a number of
                    months. `n` must be a positive integer. To set
                    ticks on the 15th of every third month, set
                    `tick0` to *2000-01-15* and `dtick` to *M3*. To
                    set ticks every 4 years, set `dtick` to *M48*
                exponentformat
                    Determines a formatting rule for the tick
                    exponents. For example, consider the number
                    1,000,000,000. If *none*, it appears as
                    1,000,000,000. If *e*, 1e+9. If *E*, 1E+9. If
                    *power*, 1x10^9 (with 9 in a super script). If
                    *SI*, 1G. If *B*, 1B.
                len
                    Sets the length of the color bar This measure
                    excludes the padding of both ends. That is, the
                    color bar length is this length minus the
                    padding on both ends.
                lenmode
                    Determines whether this color bar's length
                    (i.e. the measure in the color variation
                    direction) is set in units of plot *fraction*
                    or in *pixels. Use `len` to set the value.
                nticks
                    Specifies the maximum number of ticks for the
                    particular axis. The actual number of ticks
                    will be chosen automatically to be less than or
                    equal to `nticks`. Has an effect only if
                    `tickmode` is set to *auto*.
                outlinecolor
                    Sets the axis line color.
                outlinewidth
                    Sets the width (in px) of the axis line.
                separatethousands
                    If "true", even 4-digit integers are separated
                showexponent
                    If *all*, all exponents are shown besides their
                    significands. If *first*, only the exponent of
                    the first tick is shown. If *last*, only the
                    exponent of the last tick is shown. If *none*,
                    no exponents appear.
                showticklabels
                    Determines whether or not the tick labels are
                    drawn.
                showtickprefix
                    If *all*, all tick labels are displayed with a
                    prefix. If *first*, only the first tick is
                    displayed with a prefix. If *last*, only the
                    last tick is displayed with a suffix. If
                    *none*, tick prefixes are hidden.
                showticksuffix
                    Same as `showtickprefix` but for tick suffixes.
                thickness
                    Sets the thickness of the color bar This
                    measure excludes the size of the padding, ticks
                    and labels.
                thicknessmode
                    Determines whether this color bar's thickness
                    (i.e. the measure in the constant color
                    direction) is set in units of plot *fraction*
                    or in *pixels*. Use `thickness` to set the
                    value.
                tick0
                    Sets the placement of the first tick on this
                    axis. Use with `dtick`. If the axis `type` is
                    *log*, then you must take the log of your
                    starting tick (e.g. to set the starting tick to
                    100, set the `tick0` to 2) except when
                    `dtick`=*L<f>* (see `dtick` for more info). If
                    the axis `type` is *date*, it should be a date
                    string, like date data. If the axis `type` is
                    *category*, it should be a number, using the
                    scale where each category is assigned a serial
                    number from zero in the order it appears.
                tickangle
                    Sets the angle of the tick labels with respect
                    to the horizontal. For example, a `tickangle`
                    of -90 draws the tick labels vertically.
                tickcolor
                    Sets the tick color.
                tickfont
                    Sets the color bar's tick label font
                tickformat
                    Sets the tick label formatting rule using d3
                    formatting mini-languages which are very
                    similar to those in Python. For numbers, see: h
                    ttps://github.com/d3/d3-format/blob/master/READ
                    ME.md#locale_format And for dates see:
                    https://github.com/d3/d3-time-
                    format/blob/master/README.md#locale_format We
                    add one item to d3's date formatter: *%{n}f*
                    for fractional seconds with n digits. For
                    example, *2016-10-13 09:15:23.456* with
                    tickformat *%H~%M~%S.%2f* would display
                    *09~15~23.46*
                tickformatstops
                    plotly.graph_objs.scatter3d.marker.colorbar.Tic
                    kformatstop instance or dict with compatible
                    properties
                ticklen
                    Sets the tick length (in px).
                tickmode
                    Sets the tick mode for this axis. If *auto*,
                    the number of ticks is set via `nticks`. If
                    *linear*, the placement of the ticks is
                    determined by a starting position `tick0` and a
                    tick step `dtick` (*linear* is the default
                    value if `tick0` and `dtick` are provided). If
                    *array*, the placement of the ticks is set via
                    `tickvals` and the tick text is `ticktext`.
                    (*array* is the default value if `tickvals` is
                    provided).
                tickprefix
                    Sets a tick label prefix.
                ticks
                    Determines whether ticks are drawn or not. If
                    **, this axis' ticks are not drawn. If
                    *outside* (*inside*), this axis' are drawn
                    outside (inside) the axis lines.
                ticksuffix
                    Sets a tick label suffix.
                ticktext
                    Sets the text displayed at the ticks position
                    via `tickvals`. Only has an effect if
                    `tickmode` is set to *array*. Used with
                    `tickvals`.
                ticktextsrc
                    Sets the source reference on plot.ly for
                    ticktext .
                tickvals
                    Sets the values at which ticks on this axis
                    appear. Only has an effect if `tickmode` is set
                    to *array*. Used with `ticktext`.
                tickvalssrc
                    Sets the source reference on plot.ly for
                    tickvals .
                tickwidth
                    Sets the tick width (in px).
                title
                    Sets the title of the color bar.
                titlefont
                    Sets this color bar's title font.
                titleside
                    Determines the location of the colorbar title
                    with respect to the color bar.
                x
                    Sets the x position of the color bar (in plot
                    fraction).
                xanchor
                    Sets this color bar's horizontal position
                    anchor. This anchor binds the `x` position to
                    the *left*, *center* or *right* of the color
                    bar.
                xpad
                    Sets the amount of padding (in px) along the x
                    direction.
                y
                    Sets the y position of the color bar (in plot
                    fraction).
                yanchor
                    Sets this color bar's vertical position anchor
                    This anchor binds the `y` position to the
                    *top*, *middle* or *bottom* of the color bar.
                ypad
                    Sets the amount of padding (in px) along the y
                    direction.

        Returns
        -------
        plotly.graph_objs.scatter3d.marker.ColorBar
        """
        return self['colorbar']

    @colorbar.setter
    def colorbar(self, val):
        self['colorbar'] = val

    # colorscale
    # ----------
    @property
    def colorscale(self):
        """
        Sets the colorscale and only has an effect if `marker.color` is
        set to a numerical array. The colorscale must be an array
        containing arrays mapping a normalized value to an rgb, rgba,
        hex, hsl, hsv, or named color string. At minimum, a mapping for
        the lowest (0) and highest (1) values are required. For
        example, `[[0, 'rgb(0,0,255)', [1, 'rgb(255,0,0)']]`. To
        control the bounds of the colorscale in color space, use
        `marker.cmin` and `marker.cmax`. Alternatively, `colorscale`
        may be a palette name string of the following list: Greys,
        YlGnBu, Greens, YlOrRd, Bluered, RdBu, Reds, Blues, Picnic,
        Rainbow, Portland, Jet, Hot, Blackbody, Earth, Electric,
        Viridis, Cividis
    
        The 'colorscale' property is a colorscale and may be
        specified as:
          - A list of 2-element lists where the first element is the
            normalized color level value (starting at 0 and ending at 1), 
            and the second item is a valid color string.
            (e.g. [[0, 'green'], [0.5, 'red'], [1.0, 'rgb(0, 0, 255)']])
          - One of the following named colorscales:
                ['Greys', 'YlGnBu', 'Greens', 'YlOrRd', 'Bluered', 'RdBu',
                'Reds', 'Blues', 'Picnic', 'Rainbow', 'Portland', 'Jet',
                'Hot', 'Blackbody', 'Earth', 'Electric', 'Viridis']

        Returns
        -------
        str
        """
        return self['colorscale']

    @colorscale.setter
    def colorscale(self, val):
        self['colorscale'] = val

    # colorsrc
    # --------
    @property
    def colorsrc(self):
        """
        Sets the source reference on plot.ly for  color .
    
        The 'colorsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['colorsrc']

    @colorsrc.setter
    def colorsrc(self, val):
        self['colorsrc'] = val

    # line
    # ----
    @property
    def line(self):
        """
        The 'line' property is an instance of Line
        that may be specified as:
          - An instance of plotly.graph_objs.scatter3d.marker.Line
          - A dict of string/value properties that will be passed
            to the Line constructor
    
            Supported dict properties:
                
                autocolorscale
                    Has an effect only if `marker.line.color` is
                    set to a numerical array. Determines whether
                    the colorscale is a default palette
                    (`autocolorscale: true`) or the palette
                    determined by `marker.line.colorscale`. In case
                    `colorscale` is unspecified or `autocolorscale`
                    is true, the default  palette will be chosen
                    according to whether numbers in the `color`
                    array are all positive, all negative or mixed.
                cauto
                    Has an effect only if `marker.line.color` is
                    set to a numerical array and `cmin`, `cmax` are
                    set by the user. In this case, it controls
                    whether the range of colors in `colorscale` is
                    mapped to the range of values in the `color`
                    array (`cauto: true`), or the `cmin`/`cmax`
                    values (`cauto: false`). Defaults to `false`
                    when `cmin`, `cmax` are set by the user.
                cmax
                    Has an effect only if `marker.line.color` is
                    set to a numerical array. Sets the upper bound
                    of the color domain. Value should be associated
                    to the `marker.line.color` array index, and if
                    set, `marker.line.cmin` must be set as well.
                cmin
                    Has an effect only if `marker.line.color` is
                    set to a numerical array. Sets the lower bound
                    of the color domain. Value should be associated
                    to the `marker.line.color` array index, and if
                    set, `marker.line.cmax` must be set as well.
                color
                    Sets the marker.line color. It accepts either a
                    specific color or an array of numbers that are
                    mapped to the colorscale relative to the max
                    and min values of the array or relative to
                    `cmin` and `cmax` if set.
                colorscale
                    Sets the colorscale and only has an effect if
                    `marker.line.color` is set to a numerical
                    array. The colorscale must be an array
                    containing arrays mapping a normalized value to
                    an rgb, rgba, hex, hsl, hsv, or named color
                    string. At minimum, a mapping for the lowest
                    (0) and highest (1) values are required. For
                    example, `[[0, 'rgb(0,0,255)', [1,
                    'rgb(255,0,0)']]`. To control the bounds of the
                    colorscale in color space, use
                    `marker.line.cmin` and `marker.line.cmax`.
                    Alternatively, `colorscale` may be a palette
                    name string of the following list: Greys,
                    YlGnBu, Greens, YlOrRd, Bluered, RdBu, Reds,
                    Blues, Picnic, Rainbow, Portland, Jet, Hot,
                    Blackbody, Earth, Electric, Viridis, Cividis
                colorsrc
                    Sets the source reference on plot.ly for  color
                    .
                reversescale
                    Has an effect only if `marker.line.color` is
                    set to a numerical array. Reverses the color
                    mapping if true (`cmin` will correspond to the
                    last color in the array and `cmax` will
                    correspond to the first color).
                width
                    Sets the width (in px) of the lines bounding
                    the marker points.

        Returns
        -------
        plotly.graph_objs.scatter3d.marker.Line
        """
        return self['line']

    @line.setter
    def line(self, val):
        self['line'] = val

    # opacity
    # -------
    @property
    def opacity(self):
        """
        Sets the marker opacity. Note that the marker opacity for
        scatter3d traces must be a scalar value for performance
        reasons. To set a blending opacity value (i.e. which is not
        transparent), set *marker.color* to an rgba color and use its
        alpha channel.
    
        The 'opacity' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self['opacity']

    @opacity.setter
    def opacity(self, val):
        self['opacity'] = val

    # reversescale
    # ------------
    @property
    def reversescale(self):
        """
        Has an effect only if `marker.color` is set to a numerical
        array. Reverses the color mapping if true (`cmin` will
        correspond to the last color in the array and `cmax` will
        correspond to the first color).
    
        The 'reversescale' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['reversescale']

    @reversescale.setter
    def reversescale(self, val):
        self['reversescale'] = val

    # showscale
    # ---------
    @property
    def showscale(self):
        """
        Has an effect only if `marker.color` is set to a numerical
        array. Determines whether or not a colorbar is displayed.
    
        The 'showscale' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['showscale']

    @showscale.setter
    def showscale(self, val):
        self['showscale'] = val

    # size
    # ----
    @property
    def size(self):
        """
        Sets the marker size (in px).
    
        The 'size' property is a number and may be specified as:
          - An int or float in the interval [0, inf]
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        int|float|numpy.ndarray
        """
        return self['size']

    @size.setter
    def size(self, val):
        self['size'] = val

    # sizemin
    # -------
    @property
    def sizemin(self):
        """
        Has an effect only if `marker.size` is set to a numerical
        array. Sets the minimum size (in px) of the rendered marker
        points.
    
        The 'sizemin' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['sizemin']

    @sizemin.setter
    def sizemin(self, val):
        self['sizemin'] = val

    # sizemode
    # --------
    @property
    def sizemode(self):
        """
        Has an effect only if `marker.size` is set to a numerical
        array. Sets the rule for which the data in `size` is converted
        to pixels.
    
        The 'sizemode' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['diameter', 'area']

        Returns
        -------
        Any
        """
        return self['sizemode']

    @sizemode.setter
    def sizemode(self, val):
        self['sizemode'] = val

    # sizeref
    # -------
    @property
    def sizeref(self):
        """
        Has an effect only if `marker.size` is set to a numerical
        array. Sets the scale factor used to determine the rendered
        size of marker points. Use with `sizemin` and `sizemode`.
    
        The 'sizeref' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['sizeref']

    @sizeref.setter
    def sizeref(self, val):
        self['sizeref'] = val

    # sizesrc
    # -------
    @property
    def sizesrc(self):
        """
        Sets the source reference on plot.ly for  size .
    
        The 'sizesrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['sizesrc']

    @sizesrc.setter
    def sizesrc(self, val):
        self['sizesrc'] = val

    # symbol
    # ------
    @property
    def symbol(self):
        """
        Sets the marker symbol type.
    
        The 'symbol' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['circle', 'circle-open', 'square', 'square-open',
                'diamond', 'diamond-open', 'cross', 'x']
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        Any|numpy.ndarray
        """
        return self['symbol']

    @symbol.setter
    def symbol(self, val):
        self['symbol'] = val

    # symbolsrc
    # ---------
    @property
    def symbolsrc(self):
        """
        Sets the source reference on plot.ly for  symbol .
    
        The 'symbolsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['symbolsrc']

    @symbolsrc.setter
    def symbolsrc(self, val):
        self['symbolsrc'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'scatter3d'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        autocolorscale
            Has an effect only if `marker.color` is set to a
            numerical array. Determines whether the colorscale is a
            default palette (`autocolorscale: true`) or the palette
            determined by `marker.colorscale`. In case `colorscale`
            is unspecified or `autocolorscale` is true, the default
            palette will be chosen according to whether numbers in
            the `color` array are all positive, all negative or
            mixed.
        cauto
            Has an effect only if `marker.color` is set to a
            numerical array and `cmin`, `cmax` are set by the user.
            In this case, it controls whether the range of colors
            in `colorscale` is mapped to the range of values in the
            `color` array (`cauto: true`), or the `cmin`/`cmax`
            values (`cauto: false`). Defaults to `false` when
            `cmin`, `cmax` are set by the user.
        cmax
            Has an effect only if `marker.color` is set to a
            numerical array. Sets the upper bound of the color
            domain. Value should be associated to the
            `marker.color` array index, and if set, `marker.cmin`
            must be set as well.
        cmin
            Has an effect only if `marker.color` is set to a
            numerical array. Sets the lower bound of the color
            domain. Value should be associated to the
            `marker.color` array index, and if set, `marker.cmax`
            must be set as well.
        color
            Sets the marker color. It accepts either a specific
            color or an array of numbers that are mapped to the
            colorscale relative to the max and min values of the
            array or relative to `cmin` and `cmax` if set.
        colorbar
            plotly.graph_objs.scatter3d.marker.ColorBar instance or
            dict with compatible properties
        colorscale
            Sets the colorscale and only has an effect if
            `marker.color` is set to a numerical array. The
            colorscale must be an array containing arrays mapping a
            normalized value to an rgb, rgba, hex, hsl, hsv, or
            named color string. At minimum, a mapping for the
            lowest (0) and highest (1) values are required. For
            example, `[[0, 'rgb(0,0,255)', [1, 'rgb(255,0,0)']]`.
            To control the bounds of the colorscale in color space,
            use `marker.cmin` and `marker.cmax`. Alternatively,
            `colorscale` may be a palette name string of the
            following list: Greys, YlGnBu, Greens, YlOrRd, Bluered,
            RdBu, Reds, Blues, Picnic, Rainbow, Portland, Jet, Hot,
            Blackbody, Earth, Electric, Viridis, Cividis
        colorsrc
            Sets the source reference on plot.ly for  color .
        line
            plotly.graph_objs.scatter3d.marker.Line instance or
            dict with compatible properties
        opacity
            Sets the marker opacity. Note that the marker opacity
            for scatter3d traces must be a scalar value for
            performance reasons. To set a blending opacity value
            (i.e. which is not transparent), set *marker.color* to
            an rgba color and use its alpha channel.
        reversescale
            Has an effect only if `marker.color` is set to a
            numerical array. Reverses the color mapping if true
            (`cmin` will correspond to the last color in the array
            and `cmax` will correspond to the first color).
        showscale
            Has an effect only if `marker.color` is set to a
            numerical array. Determines whether or not a colorbar
            is displayed.
        size
            Sets the marker size (in px).
        sizemin
            Has an effect only if `marker.size` is set to a
            numerical array. Sets the minimum size (in px) of the
            rendered marker points.
        sizemode
            Has an effect only if `marker.size` is set to a
            numerical array. Sets the rule for which the data in
            `size` is converted to pixels.
        sizeref
            Has an effect only if `marker.size` is set to a
            numerical array. Sets the scale factor used to
            determine the rendered size of marker points. Use with
            `sizemin` and `sizemode`.
        sizesrc
            Sets the source reference on plot.ly for  size .
        symbol
            Sets the marker symbol type.
        symbolsrc
            Sets the source reference on plot.ly for  symbol .
        """

    def __init__(
        self,
        autocolorscale=None,
        cauto=None,
        cmax=None,
        cmin=None,
        color=None,
        colorbar=None,
        colorscale=None,
        colorsrc=None,
        line=None,
        opacity=None,
        reversescale=None,
        showscale=None,
        size=None,
        sizemin=None,
        sizemode=None,
        sizeref=None,
        sizesrc=None,
        symbol=None,
        symbolsrc=None,
        **kwargs
    ):
        """
        Construct a new Marker object
        
        Parameters
        ----------
        autocolorscale
            Has an effect only if `marker.color` is set to a
            numerical array. Determines whether the colorscale is a
            default palette (`autocolorscale: true`) or the palette
            determined by `marker.colorscale`. In case `colorscale`
            is unspecified or `autocolorscale` is true, the default
            palette will be chosen according to whether numbers in
            the `color` array are all positive, all negative or
            mixed.
        cauto
            Has an effect only if `marker.color` is set to a
            numerical array and `cmin`, `cmax` are set by the user.
            In this case, it controls whether the range of colors
            in `colorscale` is mapped to the range of values in the
            `color` array (`cauto: true`), or the `cmin`/`cmax`
            values (`cauto: false`). Defaults to `false` when
            `cmin`, `cmax` are set by the user.
        cmax
            Has an effect only if `marker.color` is set to a
            numerical array. Sets the upper bound of the color
            domain. Value should be associated to the
            `marker.color` array index, and if set, `marker.cmin`
            must be set as well.
        cmin
            Has an effect only if `marker.color` is set to a
            numerical array. Sets the lower bound of the color
            domain. Value should be associated to the
            `marker.color` array index, and if set, `marker.cmax`
            must be set as well.
        color
            Sets the marker color. It accepts either a specific
            color or an array of numbers that are mapped to the
            colorscale relative to the max and min values of the
            array or relative to `cmin` and `cmax` if set.
        colorbar
            plotly.graph_objs.scatter3d.marker.ColorBar instance or
            dict with compatible properties
        colorscale
            Sets the colorscale and only has an effect if
            `marker.color` is set to a numerical array. The
            colorscale must be an array containing arrays mapping a
            normalized value to an rgb, rgba, hex, hsl, hsv, or
            named color string. At minimum, a mapping for the
            lowest (0) and highest (1) values are required. For
            example, `[[0, 'rgb(0,0,255)', [1, 'rgb(255,0,0)']]`.
            To control the bounds of the colorscale in color space,
            use `marker.cmin` and `marker.cmax`. Alternatively,
            `colorscale` may be a palette name string of the
            following list: Greys, YlGnBu, Greens, YlOrRd, Bluered,
            RdBu, Reds, Blues, Picnic, Rainbow, Portland, Jet, Hot,
            Blackbody, Earth, Electric, Viridis, Cividis
        colorsrc
            Sets the source reference on plot.ly for  color .
        line
            plotly.graph_objs.scatter3d.marker.Line instance or
            dict with compatible properties
        opacity
            Sets the marker opacity. Note that the marker opacity
            for scatter3d traces must be a scalar value for
            performance reasons. To set a blending opacity value
            (i.e. which is not transparent), set *marker.color* to
            an rgba color and use its alpha channel.
        reversescale
            Has an effect only if `marker.color` is set to a
            numerical array. Reverses the color mapping if true
            (`cmin` will correspond to the last color in the array
            and `cmax` will correspond to the first color).
        showscale
            Has an effect only if `marker.color` is set to a
            numerical array. Determines whether or not a colorbar
            is displayed.
        size
            Sets the marker size (in px).
        sizemin
            Has an effect only if `marker.size` is set to a
            numerical array. Sets the minimum size (in px) of the
            rendered marker points.
        sizemode
            Has an effect only if `marker.size` is set to a
            numerical array. Sets the rule for which the data in
            `size` is converted to pixels.
        sizeref
            Has an effect only if `marker.size` is set to a
            numerical array. Sets the scale factor used to
            determine the rendered size of marker points. Use with
            `sizemin` and `sizemode`.
        sizesrc
            Sets the source reference on plot.ly for  size .
        symbol
            Sets the marker symbol type.
        symbolsrc
            Sets the source reference on plot.ly for  symbol .

        Returns
        -------
        Marker
        """
        super(Marker, self).__init__('marker')

        # Import validators
        # -----------------
        from plotly.validators.scatter3d import (marker as v_marker)

        # Initialize validators
        # ---------------------
        self._validators['autocolorscale'] = v_marker.AutocolorscaleValidator()
        self._validators['cauto'] = v_marker.CautoValidator()
        self._validators['cmax'] = v_marker.CmaxValidator()
        self._validators['cmin'] = v_marker.CminValidator()
        self._validators['color'] = v_marker.ColorValidator()
        self._validators['colorbar'] = v_marker.ColorBarValidator()
        self._validators['colorscale'] = v_marker.ColorscaleValidator()
        self._validators['colorsrc'] = v_marker.ColorsrcValidator()
        self._validators['line'] = v_marker.LineValidator()
        self._validators['opacity'] = v_marker.OpacityValidator()
        self._validators['reversescale'] = v_marker.ReversescaleValidator()
        self._validators['showscale'] = v_marker.ShowscaleValidator()
        self._validators['size'] = v_marker.SizeValidator()
        self._validators['sizemin'] = v_marker.SizeminValidator()
        self._validators['sizemode'] = v_marker.SizemodeValidator()
        self._validators['sizeref'] = v_marker.SizerefValidator()
        self._validators['sizesrc'] = v_marker.SizesrcValidator()
        self._validators['symbol'] = v_marker.SymbolValidator()
        self._validators['symbolsrc'] = v_marker.SymbolsrcValidator()

        # Populate data dict with properties
        # ----------------------------------
        self.autocolorscale = autocolorscale
        self.cauto = cauto
        self.cmax = cmax
        self.cmin = cmin
        self.color = color
        self.colorbar = colorbar
        self.colorscale = colorscale
        self.colorsrc = colorsrc
        self.line = line
        self.opacity = opacity
        self.reversescale = reversescale
        self.showscale = showscale
        self.size = size
        self.sizemin = sizemin
        self.sizemode = sizemode
        self.sizeref = sizeref
        self.sizesrc = sizesrc
        self.symbol = symbol
        self.symbolsrc = symbolsrc

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**kwargs)