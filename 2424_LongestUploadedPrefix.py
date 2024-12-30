class LUPrefix:
    def __init__(self, n: int):
        self.interv = {} # map, K: start, V: end of an interval
        self.rev = {} # mirror map for O(1) previous key lookup

    def upload(self, video: int) -> None:
        kPrev = self.rev[video-1] if video-1 in self.rev else None
        kNext = video+1 if video+1 in self.interv else None
        if kPrev and kNext: # if bridging two intervals
            del self.rev[self.interv[kPrev]]
            self.interv[kPrev] = self.interv[kNext]
            self.rev[self.interv[kNext]] = kPrev
            del self.interv[kNext]
        elif kNext: # if prepending
            self.interv[video] = self.interv[kNext]
            self.rev[self.interv[kNext]] = video
            del self.interv[kNext]
        elif kPrev: # if appending
            del self.rev[self.interv[kPrev]]
            self.interv[kPrev] = video
            self.rev[video] = kPrev
        else: # if isolated
            self.interv[video] = video
            self.rev[video] = video

    def longest(self) -> int:
        if 1 in self.interv:
            return self.interv[1]
        return 0
