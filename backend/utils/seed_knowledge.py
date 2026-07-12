from pathlib import Path
from utils.config import settings

DEFAULT_KNOWLEDGE = """
# Sports Equipment Knowledge Base

## Cricket Bat
Cricket bats are normally made from English willow or Kashmir willow. English willow is preferred by advanced players because it is lighter and offers better rebound. Beginners can use Kashmir willow because it is economical and durable. A new willow bat should be knocked in before match use. Accessories include bat covers, grips, toe guards, anti-scuff sheets, bat oil, and mallets.

## Cricket Ball
Cricket balls have leather covers, cork cores, and stitched seams. Red balls are commonly used in longer formats, white balls in limited overs, and pink balls for day-night matches. Hard-ball cricket requires helmet, gloves, pads, abdominal guard, and thigh guard.

## Football
Football size depends on age group. Size 3 is common for young children, size 4 for youth players, and size 5 for adults. Match balls should maintain correct air pressure. Accessories include pump, needle, shin guards, ball bag, and cones.

## Basketball
Basketball sizes vary by age and competition. Size 7 is common for men's basketball, size 6 for women's basketball, and size 5 for youth. Indoor balls often use composite leather, while outdoor balls use durable rubber.

## Volleyball
Volleyballs are designed for controlled contact using forearms, fingers, and palms. Indoor volleyballs are slightly heavier and smoother, while beach volleyballs are softer and more weather-resistant. Knee pads and proper shoes reduce injury risk.

## Tennis Racket
Tennis rackets vary by head size, weight, balance, grip size, and string tension. Beginners usually benefit from larger head sizes and lighter frames. Strings and grips should be replaced when worn.

## Badminton Racket
Badminton rackets are lightweight and commonly made from graphite or aluminum. String tension affects control and power. Beginners should use moderate tension and a flexible shaft. Accessories include grip, strings, shuttle tubes, and racket cover.

## Shuttlecock
Feather shuttlecocks give better flight but wear quickly. Nylon shuttlecocks are more durable and suitable for beginners. Shuttles should be stored away from moisture and heat.

## Hockey Stick
Hockey sticks may be wooden, fiberglass, carbon fiber, or composite. More carbon provides power but may reduce touch for beginners. Players should use shin guards, mouthguards, and proper grip tape.

## Baseball Bat
Baseball bats may be wood, aluminum, or composite. Bat length and weight must match player strength and league rules. Dented aluminum bats and cracked wooden bats are unsafe.

## Baseball Glove
Baseball gloves require breaking in. Leather gloves provide better feel and durability. Glove oil should be used sparingly. Loose laces must be repaired before play.

## Goalkeeper Gloves
Goalkeeper gloves use latex palms for grip. Match gloves give superior grip but wear faster. Training gloves are more durable. Gloves should be cleaned after use and dried naturally away from sunlight.

## Helmet
Sports helmets protect against head impacts. A helmet should fit firmly, have certified protection, and be replaced after major impact. Cricket helmets should include a proper face grille.

## Golf Club
Golf clubs include drivers, woods, irons, wedges, and putters. Shaft flex, club length, and grip size affect performance. Beginners usually need forgiving cavity-back irons and proper club fitting.

## Sports Shoes
Sports shoes should match the sport surface and movement pattern. Running shoes focus on cushioning, basketball shoes on ankle support, football boots on traction, and court shoes on lateral stability. Worn soles increase injury risk.

## Fake Equipment Detection Guidelines
Common warning signs of fake sports equipment include unusually low price, poor stitching, weak logo printing, incorrect serial numbers, bad packaging, uneven weight, poor grip quality, and sellers without proper invoices. Verification should include checking official brand tags, QR codes, authorized dealer information, and warranty documents.

## Maintenance Guidelines
Equipment should be cleaned after use, dried naturally, stored in a protective cover, and inspected for cracks or deformation. Leather and willow equipment need special care. Inflatable balls must be maintained at the correct pressure. Shoes should be dried at room temperature and not under direct heat.
"""

def ensure_default_files() -> None:
    kb_dir = settings.resolved_knowledge_base_dir
    kb_dir.mkdir(parents=True, exist_ok=True)
    path = kb_dir / "equipment_knowledge.md"
    if not path.exists():
        path.write_text(DEFAULT_KNOWLEDGE.strip() + "\n", encoding="utf-8")
    settings.resolved_vector_db_dir.mkdir(parents=True, exist_ok=True)
