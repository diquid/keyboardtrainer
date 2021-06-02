class checksymbols(object):
    def on_type_entry_activate(self, *args):
        if self.start_time:
            delta = time.time() - self.start_time

            cur_text = unicode(self.type_entry.get_text())

            errors = len(self.totype_text) - len(cur_text)
            for i, c in enumerate(cur_text):
                if c != self.totype_text[i]:
                    errors += 1

            err = self.get_error(self.typed_chars)
            while err:
                volume = self.filler.get_available_parts_for(err)
                if volume > 0.005:
                    self.filler.change_distribution(err, 0.8, True)
                    self.retype_lb.set_text(err)
                    break

                err = err[1:]
            else:
                self.filler.reset_distribution()
                self.retype_lb.set_text('')

            cpm = int((len(cur_text) + 1) * 60.0 / delta)
            accuracy = int((len(self.totype_text) - errors) * 100.0 / len(self.totype_text))
            self.stat_lb.set_text('%d / %d%%' % (cpm, accuracy))

            if self.filler.fullname:
                self.stat.log(self.filler.fullname, cpm, accuracy)

        self.fill()