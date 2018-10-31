import sys
import pygame

from arrow import Arrow
from statarrow import Statarrow
import mapLoader as ml

def create_fleet(ml, arrow_group):
    map = ml.MapLoader()
    """Create a full fleet of aliens."""
    # Create an alien, and find number of aliens in a row.
    arrow = Arrow(type, x,y, width, height, speed)

    # Create the fleet of aliens.
    for i in range(map.getSecs):
        create_alien(screen, arrow_group, i)

def create_arrow(arrow_group, i):
    """Create an alien, and place it in the row."""
    arrow = Arrow(type, x,y, width, height, speed)
    arrow.y = alien.height + 2 * alien.height * i
    arrow_group.add(arrow)



'''
def check_bullet_alien_collisions(statarrows, arrows):
    """Respond to bullet-alien collisions."""
    # Remove any bullets and aliens that have collided.
    collisions = pygame.sprite.groupcollide(statarrows, arrows, True, True)

    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        # If the entire fleet is destroyed, start a new level.
        bullets.empty()
        ai_settings.increase_speed()

        # Increase level.
        stats.level += 1
        sb.prep_level()

        create_fleet(ai_settings, screen, ship, aliens)
'''_group
