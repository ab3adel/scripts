from cairosvg import svg2png

svg_Code ="""
<svg xmlns="http://www.w3.org/2000/svg" width="37.969" height="33.5" viewBox="0 0 37.969 33.5"><defs><style>
.a{fill:none;stroke:#000;stroke-linecap:round;stroke-linejoin:round;stroke-width:3px;fill-rule:evenodd;}
</style></defs><path class="a" 
d="M33.821,3.695a9.2,9.2,0,0,0-13.015,0L19.033,5.468,17.259,3.695A9
.2,9.2,0,1,0,4.244,16.71l1.773,1.773L19.033,31.5,32.048,18.483l1.773-1.773a9.
2,9.2,0,0,0,0-13.015Z" transform="translate(-0.049 0.502)"/></svg>
"""

svg2png(bytestring=svg_Code,write_to='img1.png')