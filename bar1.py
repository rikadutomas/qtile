from libqtile.bar import Bar
from libqtile import widget
from libqtile.widget.battery import Battery
from libqtile.widget.clock import Clock
from libqtile.widget.cpu import CPU
from libqtile.widget.currentlayout import CurrentLayout
from libqtile.widget.groupbox import GroupBox
from libqtile.widget.memory import Memory
from libqtile.widget.net import Net
from libqtile.widget.spacer import Spacer
from libqtile.widget.systray import Systray
from libqtile.widget.window_count import WindowCount
from libqtile.widget.windowname import WindowName
from libqtile.widget.battery import BatteryIcon

from unicodes import left_half_circle, right_arrow, left_arrow, right_half_circle
from colors import nord_fox, gruvbox

BAR_HEIGHT = 28
# BAR_MARGIN = 5

bar = Bar([

    ##Left Side

    GroupBox(
        disable_drag=True,
        active=nord_fox['green'],
        inactive=nord_fox['black'],
        # active=nord_fox['magenta'],
        # inactive=nord_fox['black'],
        highlight_method='line',
        block_highlight_text_color=nord_fox['fg_gutter'],
        borderwidth=0,
        highlight_color=nord_fox['white'],
        background=nord_fox['bg'],
        # spacing=2
    ),
    right_arrow(nord_fox['red'], nord_fox['bg']),
    CurrentLayout(
        background=nord_fox['red'],
        foreground=nord_fox['white'],
        margin=10,
    ),

    right_arrow(nord_fox['fg_gutter'], nord_fox['red']),
    WindowCount(
        text_format=' {num}',
        background=nord_fox['fg_gutter'],
        foreground=nord_fox['white'],
        show_zero=True,
    ),
    right_arrow(nord_fox['bg'], nord_fox['fg_gutter']),

    WindowName(
        background=nord_fox['bg'],
        foreground=nord_fox['fg']
    ),

    ##Right Side

    left_arrow(nord_fox['bg'], nord_fox['black']),
    CPU(
        format=' {freq_current}GHz {load_percent}%',
        background=nord_fox['black'],
        foreground=nord_fox['pink'],
    ),

    Memory(
        format=' {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
        background=nord_fox['black'],
        foreground=nord_fox['cyan']
    ),

    Net(
        background=nord_fox['black'],
        foreground=nord_fox['green']
    ),
    left_arrow(nord_fox['black'], gruvbox['fg3']),
    widget.BatteryIcon(
        scale=1.1,
        background=gruvbox['fg3'],
    ),
    Battery(
        background=gruvbox['fg3'],
        #format='{char} {percent:2.0%} {hour:d}:{min:02d}'
        format='{percent:2.0%} {hour}:{min}'
    ),

    left_arrow(gruvbox['fg3'], nord_fox['black']),
    Systray(
        background=nord_fox['black'],
        icon_size=20
    ),
    left_arrow(nord_fox['black'], nord_fox['fg_gutter']),
    Clock(
        background=nord_fox['fg_gutter'],
        foreground=nord_fox['white'],
        format=' %Y-%m-%d %a %H:%M'
    ),



],
    # background=nord_fox['bg'],
    size=BAR_HEIGHT,
    # margin=8,
)
