import random
import time
import threading
import pygame

class StreamingSimulator:
    def __init__(self, streamer_name, platform="Twitch", stream_title="Live Streaming!", category="Just Chatting"):
        self.streamer_name = streamer_name
        self.platform = platform
        self.stream_title = stream_title
        self.category = category
        self.viewers = 0
        self.peak_viewers = 0
        self.chat_messages = []
        self.donations = []
        self.subscribers = 0
        self.follows = 0
        self.raids = 0
        self.emotes_used = 0
        self.bits_used = 0
        self.polls = []
        self.hype_trains = 0
        self.uptime = 0
        self.is_live = False
        self.total_donations = 0.0
        self.top_donors = []
        self.moderators = ["ModBot", "ChatGuard"]
        self.banned_users = []
        self.platform_messages = {
            "Twitch": ["LUL", "PogChamp", "Kappa", "Subbed!", "Raid incoming!", "Cheer100", "Gift sub!"],
            "YouTube": ["Pinned message", "Super Chat", "Like!", "Subscribe!", "Live chat", "Donation", "Membership"],
            "StreamApp": ["Custom emote", "Boost!", "Follow!", "Donate!", "Raid!", "Bits!", "Sub gift!"]
        }
        # Pygame setup
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 700))
        pygame.display.set_caption(f"{self.streamer_name}'s Stream Simulator - {self.platform}")
        self.font = pygame.font.SysFont(None, 24)
        self.small_font = pygame.font.SysFont(None, 18)
        self.clock = pygame.time.Clock()

    def start_stream(self):
        self.is_live = True
        self.viewers = random.randint(10, 100)

    def update_top_donors(self):
        # Sort donations by amount descending
        sorted_donations = sorted(self.donations, key=lambda x: x[1], reverse=True)
        self.top_donors = sorted_donations[:5]  # Top 5

    def display(self):
        self.screen.fill((0, 0, 0))  # Black background
        y = 10
        # Stream info
        text = self.font.render(f"Streamer: {self.streamer_name} on {self.platform}", True, (255, 255, 255))
        self.screen.blit(text, (10, y))
        y += 30
        text = self.font.render(f"Title: {self.stream_title}", True, (255, 255, 255))
        self.screen.blit(text, (10, y))
        y += 30
        text = self.font.render(f"Category: {self.category}", True, (255, 255, 255))
        self.screen.blit(text, (10, y))
        y += 30
        text = self.font.render(f"Uptime: {self.uptime}s", True, (255, 255, 255))
        self.screen.blit(text, (10, y))
        y += 30
        text = self.font.render(f"Viewers: {self.viewers} (Peak: {self.peak_viewers})", True, (255, 255, 255))
        self.screen.blit(text, (10, y))
        y += 30
        text = self.font.render(f"Donations: ${self.total_donations:.2f}", True, (255, 255, 255))
        self.screen.blit(text, (10, y))
        y += 30
        text = self.font.render(f"Subscribers: {self.subscribers}", True, (255, 255, 255))
        self.screen.blit(text, (10, y))
        y += 30
        text = self.font.render(f"Follows: {self.follows}", True, (255, 255, 255))
        self.screen.blit(text, (10, y))
        y += 30
        text = self.font.render(f"Raids: {self.raids}", True, (255, 255, 255))
        self.screen.blit(text, (10, y))
        y += 30
        text = self.font.render(f"Emotes: {self.emotes_used}", True, (255, 255, 255))
        self.screen.blit(text, (10, y))
        y += 30
        text = self.font.render(f"Bits: {self.bits_used}", True, (255, 255, 255))
        self.screen.blit(text, (10, y))
        y += 30
        text = self.font.render(f"Hype Trains: {self.hype_trains}", True, (255, 255, 255))
        self.screen.blit(text, (10, y))
        y += 40
        # Top donors
        text = self.small_font.render("Top Donors:", True, (255, 0, 255))
        self.screen.blit(text, (10, y))
        y += 20
        for donor, amount in self.top_donors[:3]:
            text = self.small_font.render(f"{donor}: ${amount:.2f}", True, (255, 255, 255))
            self.screen.blit(text, (10, y))
            y += 20
        y += 10
        # Chat
        text = self.small_font.render("Recent Chat:", True, (255, 255, 0))
        self.screen.blit(text, (400, 10))
        y_chat = 40
        for msg in self.chat_messages[-15:]:  # Last 15 messages
            text = self.small_font.render(msg, True, (255, 255, 255))
            self.screen.blit(text, (400, y_chat))
            y_chat += 20
            if y_chat > 650:
                break
        # Moderators
        text = self.small_font.render("Mods:", True, (0, 255, 0))
        self.screen.blit(text, (10, 600))
        mod_text = ", ".join(self.moderators)
        text = self.small_font.render(mod_text, True, (255, 255, 255))
        self.screen.blit(text, (10, 620))
        pygame.display.flip()

    def simulate_viewers(self):
        while self.is_live:
            change = random.randint(-5, 15)
            self.viewers = max(0, self.viewers + change)
            self.peak_viewers = max(self.peak_viewers, self.viewers)
            time.sleep(random.uniform(1, 5))

    def simulate_chat(self):
        viewer_names = ["User1", "GamerPro", "ChatBot", "RandomViewer", "Fan123", "Lurker", "ShoutoutGuy", "EmoteLover", "SubGifter", "RaidLeader"]
        base_messages = [
            "Great stream!",
            "Love the content!",
            "Can you play that game?",
            "Nice!",
            "Hello from [country]!",
            "What's your setup?",
            "First time here!",
            "Keep it up!",
            "Amazing gameplay!",
            "Chat is lit!"
        ]
        platform_specific = self.platform_messages.get(self.platform, [])
        messages = base_messages + platform_specific
        while self.is_live:
            name = random.choice(viewer_names)
            msg = random.choice(messages)
            if "Donated" in msg or "Super Chat" in msg:
                amount = random.uniform(1, 50)
                self.donations.append((name, amount))
                self.total_donations += amount
                self.update_top_donors()
                msg = f"{name} donated ${amount:.2f}!"
            elif "Cheer" in msg:
                bits = random.randint(100, 1000)
                self.bits_used += bits
                msg = f"{name} cheered {bits} bits!"
            elif "Gift sub" in msg:
                gifted_subs = random.randint(1, 5)
                self.subscribers += gifted_subs
                msg = f"{name} gifted {gifted_subs} subs!"
            elif "Subbed" in msg or "Subscribe" in msg or "Membership" in msg:
                self.subscribers += 1
                msg = f"{name} subscribed!"
            elif "Raid" in msg:
                raid_viewers = random.randint(10, 100)
                self.raids += 1
                self.viewers += raid_viewers
                msg = f"{name} raided with {raid_viewers} viewers!"
            elif msg in ["LUL", "PogChamp", "Kappa", "Custom emote"]:
                self.emotes_used += 1
                msg = f"{name}: {msg}"
            else:
                msg = f"{name}: {msg}"
            self.chat_messages.append(msg)
            # print(msg)  # Removed for window display
            time.sleep(random.uniform(0.5, 3))

    def simulate_follows(self):
        while self.is_live:
            if random.random() < 0.1:  # 10% chance per interval
                self.follows += 1
                # print(f"New follow: {random.choice(['Anon', 'ViewerX', 'FanY'])} followed!")  # Removed
            time.sleep(random.uniform(5, 15))

    def simulate_polls(self):
        while self.is_live:
            if random.random() < 0.02:  # 2% chance
                poll_options = ["Option A", "Option B", "Option C"]
                winner = random.choice(poll_options)
                self.polls.append(f"Poll ended: {winner} won!")
                self.chat_messages.append(f"Poll: {winner} won!")
            time.sleep(random.uniform(20, 60))

    def simulate_hype_train(self):
        while self.is_live:
            if random.random() < 0.01:  # 1% chance
                self.hype_trains += 1
                self.chat_messages.append("Hype train started! Choo choo!")
                # Simulate hype
                for _ in range(random.randint(5, 15)):
                    if not self.is_live:
                        break
                    self.emotes_used += random.randint(1, 10)
                    time.sleep(1)
                self.chat_messages.append("Hype train ended!")
            time.sleep(random.uniform(30, 120))

    def run_simulation(self, duration=60):
        self.start_stream()
        viewer_thread = threading.Thread(target=self.simulate_viewers)
        chat_thread = threading.Thread(target=self.simulate_chat)
        follows_thread = threading.Thread(target=self.simulate_follows)
        polls_thread = threading.Thread(target=self.simulate_polls)
        hype_thread = threading.Thread(target=self.simulate_hype_train)
        viewer_thread.start()
        chat_thread.start()
        follows_thread.start()
        polls_thread.start()
        hype_thread.start()
        start_time = time.time()
        running = True
        while running and (time.time() - start_time < duration):
            self.uptime = int(time.time() - start_time)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.display()
            self.clock.tick(30)  # 30 FPS
        self.is_live = False
        viewer_thread.join()
        chat_thread.join()
        follows_thread.join()
        polls_thread.join()
        hype_thread.join()
        self.stop_stream()
        # Final display
        self.display()
        # Wait for user to close
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
            self.clock.tick(30)
        pygame.quit()

if __name__ == "__main__":
    simulator = StreamingSimulator("StreamerGuy", "Twitch", "Playing GTA V - Ultimate Chaos!", "Gaming")
    simulator.run_simulation(30)  # Run for 30 seconds
