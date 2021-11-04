# This is an interface with all of the necessary function for implementing a correct languagescheme.
# Import this interface to a new class, and fill out all the function with your desired language.
from abc import ABCMeta, abstractmethod


class LanguageInterface(ABCMeta):
# First part of interface concerns the loginscreen.
# Each additional aspect of the UI can be found under the following sections(search for stated keyword):
# UserHome - the UI the user arrives at when gets logged in,
# SearchScreen - the UI that pops up when the user clicks to search for toys
# MessageScreen - the UI that is used when users are messaging each other about toys
# MapScreen - the UI that is used when user is looking on the map to find where toys are located

    @abstractmethod
    def welcome_message(self):
        pass

    @abstractmethod
    def exit_button(self):
        pass

    @abstractmethod
    def login_button(self):
        pass

