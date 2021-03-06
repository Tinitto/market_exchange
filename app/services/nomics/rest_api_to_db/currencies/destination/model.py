"""
Model for currencies supported by the Nomics API
https://nomics.com/docs/#operation/getCurrencies
"""
import sqlalchemy as orm

from ...abstract.destinations.nomics_live_db.connection import NomicsDbConnectionConfig
from ...abstract.destinations.nomics_live_db.model import NomicsDatabaseBaseModel


class Currencies(NomicsDatabaseBaseModel):
    """
    Database model for all currencies supported by the nomics API from the /currencies endpoint
    """
    __tablename__ = 'currencies'
    _db_configuration = NomicsDbConnectionConfig()
    __table_args__ = {'schema': 'currencies'}

    id = orm.Column(orm.Text, primary_key=True)
    original_symbol = orm.Column(orm.Text)
    name = orm.Column(orm.Text)
    description = orm.Column(orm.Text)
    website_url = orm.Column(orm.Text)
    logo_url = orm.Column(orm.Text)
    blog_url = orm.Column(orm.Text)
    discord_url = orm.Column(orm.Text)
    facebook_url = orm.Column(orm.Text)
    github_url = orm.Column(orm.Text)
    medium_url = orm.Column(orm.Text)
    reddit_url = orm.Column(orm.Text)
    telegram_url = orm.Column(orm.Text)
    twitter_url = orm.Column(orm.Text)
    whitepaper_url = orm.Column(orm.Text)
    youtube_url = orm.Column(orm.Text)
    linkedin_url = orm.Column(orm.Text)
    bitcointalk_url = orm.Column(orm.Text)
    block_explorer_url = orm.Column(orm.Text)
    replaced_by = orm.Column(orm.Text)
    markets_count = orm.Column(orm.Text)
    cryptocontrol_coin_id = orm.Column(orm.Text)
