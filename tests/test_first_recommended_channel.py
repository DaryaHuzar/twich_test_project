from pages.home_page import HomePage
from pages.first_recommended_channel_page import FirstRecommendedChannel


def test_dark_mode_toggle(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_channel()
    first_rec_channel = FirstRecommendedChannel(driver)
    first_rec_channel.click_user_menu_button()
    first_rec_channel.activate_dark_mode_toggle()
    assert first_rec_channel.dark_mode().is_enabled()


def test_change_language(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_channel()
    first_rec_channel = FirstRecommendedChannel(driver)
    first_rec_channel.click_user_menu_button()
    first_rec_channel.click_language_button()
    first_rec_channel.chose_english_language()
    assert first_rec_channel.navigation_in_english().is_displayed()


def test_theatre_mode_button(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_channel()
    first_rec_channel = FirstRecommendedChannel(driver)
    first_rec_channel.click_theatre_mode_button(driver)
    assert first_rec_channel.theatre_mode_activated()


def test_full_screen_mode_button(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_channel()
    first_rec_channel = FirstRecommendedChannel(driver)
    first_rec_channel.click_full_screen_button(driver)
    assert first_rec_channel.full_screen_mode_activated()


def test_change_video_quality(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_channel()
    first_rec_channel = FirstRecommendedChannel(driver)
    first_rec_channel.click_settings_button(driver)
    first_rec_channel.click_quality_button()
    first_rec_channel.select_1080p60_quality()
    assert first_rec_channel.quality_video_change_check(driver) == '1080p60 (источник)'


def test_mini_player_window(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_channel()
    first_rec_channel = FirstRecommendedChannel(driver)
    first_rec_channel.click_settings_button(driver)
    first_rec_channel.click_advanced_button()
    first_rec_channel.mini_player_activate()
    first_rec_channel.click_view_button()
    assert first_rec_channel.check_mini_player_window().is_displayed()


def test_pause_stream(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_channel()
    first_rec_channel = FirstRecommendedChannel(driver)
    first_rec_channel.pause_stream(driver)
    assert first_rec_channel.show_pausing_message().is_displayed()


def test_muting_stream(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_channel()
    first_rec_channel = FirstRecommendedChannel(driver)
    first_rec_channel.muting_stream(driver)
    assert first_rec_channel.stream_is_muted(driver) == 'Stream is muted!'


def test_video_statistics(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_channel()
    first_rec_channel = FirstRecommendedChannel(driver)
    first_rec_channel.click_settings_button(driver)
    first_rec_channel.click_advanced_button()
    first_rec_channel.click_video_statistics_button()
    assert first_rec_channel.check_video_statistics_window().is_displayed()


def test_report_a_bug_selection(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_channel()
    first_rec_channel = FirstRecommendedChannel(driver)
    first_rec_channel.click_settings_button(driver)
    first_rec_channel.click_report_a_bug()
    first_rec_channel.select_a_bug()
    assert first_rec_channel.error_option_selected().is_selected()


def test_show_hotkeys_button(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_channel()
    first_rec_channel = FirstRecommendedChannel(driver)
    first_rec_channel.click_settings_button(driver)
    first_rec_channel.click_show_hotkeys()
    assert first_rec_channel.list_of_hotkeys().is_displayed()


def test_community_button(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_channel()
    first_rec_channel = FirstRecommendedChannel(driver)
    first_rec_channel.open_chat()
    first_rec_channel.click_community_button()
    assert first_rec_channel.info_about_community().is_displayed()


def test_chat_filtration_button(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_channel()
    first_rec_channel = FirstRecommendedChannel(driver)
    first_rec_channel.open_chat()
    first_rec_channel.click_chat_settings_button()
    first_rec_channel.enable_chat_filtration()
    assert first_rec_channel.chat_filtration().is_enabled()


def test_community_points_button(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_channel()
    first_rec_channel = FirstRecommendedChannel(driver)
    first_rec_channel.open_chat()
    first_rec_channel.click_community_points_button()
    assert first_rec_channel.channel_points_reward().is_displayed()


def test_follow_button(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_channel()
    first_rec_channel = FirstRecommendedChannel(driver)
    first_rec_channel.click_follow_button(driver)
    assert first_rec_channel.join_to_twitch_window().is_displayed()


def test_subscribe_button(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_channel()
    first_rec_channel = FirstRecommendedChannel(driver)
    first_rec_channel.click_subscribe_button()
    assert first_rec_channel.subscription_info().is_displayed()


def test_paid_subscribe_button(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_channel()
    first_rec_channel = FirstRecommendedChannel(driver)
    first_rec_channel.click_subscribe_button()
    first_rec_channel.click_paid_subscription()
    assert first_rec_channel.sign_in_window().is_displayed()


def test_donate_subscription_button(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_channel()
    first_rec_channel = FirstRecommendedChannel(driver)
    first_rec_channel.click_subscribe_button()
    first_rec_channel.click_donate_subscription()
    assert first_rec_channel.gift_for_community_window().is_displayed()


def test_show_love_gif_in_gift_theme(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_channel()
    first_rec_channel = FirstRecommendedChannel(driver)
    first_rec_channel.click_subscribe_button()
    first_rec_channel.click_donate_subscription()
    first_rec_channel.click_show_love_gift_theme()
    assert first_rec_channel.show_love_gif().is_displayed()


def test_party_gif_in_gift_theme(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_channel()
    first_rec_channel = FirstRecommendedChannel(driver)
    first_rec_channel.click_subscribe_button()
    first_rec_channel.click_donate_subscription()
    first_rec_channel.click_party_gift_theme()
    assert first_rec_channel.party_gif().is_displayed()


def test_lul_gif_in_gift_theme(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_channel()
    first_rec_channel = FirstRecommendedChannel(driver)
    first_rec_channel.click_subscribe_button()
    first_rec_channel.click_donate_subscription()
    first_rec_channel.click_lul_gift_theme()
    assert first_rec_channel.lul_gif().is_displayed()


def test_biblethump_gif_in_gift_theme(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_channel()
    first_rec_channel = FirstRecommendedChannel(driver)
    first_rec_channel.click_subscribe_button()
    first_rec_channel.click_donate_subscription()
    first_rec_channel.click_biblethump_gift_theme()
    assert first_rec_channel.biblethump_gif().is_displayed()


def test_share_with_button(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_channel()
    first_rec_channel = FirstRecommendedChannel(driver)
    first_rec_channel.click_share_button()
    assert first_rec_channel.share_with_field().is_displayed()


def test_report_translation_button(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_channel()
    first_rec_channel = FirstRecommendedChannel(driver)
    first_rec_channel.click_report_button()
    first_rec_channel.click_report_translation_button()
    assert first_rec_channel.sign_in_window().is_displayed()


def test_report_other_button(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_channel()
    first_rec_channel = FirstRecommendedChannel(driver)
    first_rec_channel.click_report_button()
    first_rec_channel.click_report_other_button()
    assert first_rec_channel.sign_in_window().is_displayed()


def test_searching_field(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_channel()
    first_rec_channel = FirstRecommendedChannel(driver)
    first_rec_channel.find_zubarefff_channel()
    assert first_rec_channel.zubarefff_channel().is_displayed()


def test_collapse_recommended_channels(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_channel()
    first_rec_channel = FirstRecommendedChannel(driver)
    first_rec_channel.click_collapse_recommended_channels()
    assert first_rec_channel.only_icons_of_streams().is_displayed()


def test_show_more_channels_button(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_channel()
    first_rec_channel = FirstRecommendedChannel(driver)
    first_rec_channel.click_show_more_channels_button()
    assert first_rec_channel.more_channels().is_displayed()


def test_logout_button(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_channel()
    first_rec_channel = FirstRecommendedChannel(driver)
    first_rec_channel.click_user_menu_button()
    first_rec_channel.click_logout_button()
    assert first_rec_channel.sign_in_window().is_displayed()
