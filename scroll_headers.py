import sublime
import sublime_plugin
import re


class ScrollCommand(sublime_plugin.WindowCommand):

    def run(self):

        settings = sublime.load_settings(
            'ScrollThroughHeaders.sublime-settings')

        header_regex = re.compile(settings.get('header_regex'))
        title_regex = re.compile(settings.get('title_regex'))

        view = self.window.active_view()
        # whole script text
        content = view.substr(sublime.Region(0, view.size() - 1))

        matches = re.finditer(header_regex, content)
        self.headers = []
        for m in matches:
            starts = m.start()
            lines_before = len(re.findall('\n', content[0:starts]))
            header = m.string[m.start():m.end()]
            header_clean = str.strip(re.findall(title_regex, header)[0])
            self.headers.append([header_clean, lines_before])

        self.window.show_quick_panel(
            items=[h[0] for h in self.headers],
            on_select=lambda x: None,
            on_highlight=self.goto_header
        )

    def goto_header(self, index):
        line = self.headers[index][1]

        view = self.window.active_view()
        pt = view.text_point(line, 0)

        view.sel().clear()
        view.sel().add(sublime.Region(pt))

        view.show_at_center(pt)
