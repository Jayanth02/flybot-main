

import os
import sys
from contextlib import contextmanager

@contextmanager
def suppress_stdout_stderr():
    """
    Suppresses stdout and stderr to avoid noisy logs.
    Typically used during pygame initialization or other
    operations that generate unnecessary console output.
    """
    with open(os.devnull, 'w') as fnull:
        old_stdout, old_stderr = sys.stdout, sys.stderr
        sys.stdout, sys.stderr = fnull, fnull
        try:
            yield
        finally:
            sys.stdout, sys.stderr = old_stdout, old_stderr

def suppress_pygame_logs():
    """
    Suppresses pygame initialization logs.
    This sets the SDL_VIDEODRIVER environment variable to 'dummy'
    and redirects output during initialization.
    """
    os.environ["SDL_VIDEODRIVER"] = "dummy"  # Prevents Pygame window from opening
    with suppress_stdout_stderr():
        import pygame
        pygame.mixer.init()
