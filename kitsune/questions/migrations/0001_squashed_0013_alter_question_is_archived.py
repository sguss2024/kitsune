# Generated by Django 4.1.7 on 2023-04-18 13:50

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import kitsune.search.models
import kitsune.sumo.models
import kitsune.tags.models


class Migration(migrations.Migration):
    replaces = [
        ("questions", "0001_initial"),
        ("questions", "0002_initial_data"),
        ("questions", "0003_auto_20150430_1304"),
        ("questions", "0004_new_aaq_waffle_flag"),
        ("questions", "0005_change_locale_sr_Cyrl_to_sr"),
        ("questions", "0006_ios_questionlocale"),
        ("questions", "0007_auto_20151110_1307"),
        ("questions", "0008_auto_20190507_1052"),
        ("questions", "0009_change_bn_BD_to_bn"),
        ("questions", "0010_auto_20190816_1824"),
        ("questions", "0011_auto_20200629_0826"),
        ("questions", "0012_aaqconfig"),
        ("questions", "0013_alter_question_is_archived"),
    ]

    initial = True

    dependencies = [
        ("products", "0001_initial"),
        ("taggit", "0001_initial"),
        ("waffle", "0001_initial"),
        ("contenttypes", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("wiki", "0012_auto_20200629_0826"),
        ("products", "0005_auto_20200629_0826"),
    ]

    operations = [
        migrations.CreateModel(
            name="Answer",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("created", models.DateTimeField(db_index=True, default=datetime.datetime.now)),
                ("content", models.TextField()),
                ("updated", models.DateTimeField(db_index=True, default=datetime.datetime.now)),
                ("page", models.IntegerField(default=1)),
                ("is_spam", models.BooleanField(default=False)),
                ("marked_as_spam", models.DateTimeField(default=None, null=True)),
                (
                    "creator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="answers",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "marked_as_spam_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="answers_marked_as_spam",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["created"],
                "permissions": (("bypass_answer_ratelimit", "Can bypass answering ratelimit"),),
            },
            bases=(models.Model, kitsune.search.models.SearchMixin),
        ),
        migrations.CreateModel(
            name="Question",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("content", models.TextField()),
                ("created", models.DateTimeField(db_index=True, default=datetime.datetime.now)),
                ("updated", models.DateTimeField(db_index=True, default=datetime.datetime.now)),
                ("num_answers", models.IntegerField(db_index=True, default=0)),
                ("is_locked", models.BooleanField(default=False)),
                ("is_archived", models.BooleanField(default=False, null=True)),
                ("num_votes_past_week", models.PositiveIntegerField(db_index=True, default=0)),
                ("is_spam", models.BooleanField(default=False)),
                ("marked_as_spam", models.DateTimeField(default=None, null=True)),
                (
                    "locale",
                    kitsune.sumo.models.LocaleField(
                        choices=[
                            ("af", "Afrikaans"),
                            ("ar", "عربي"),
                            ("az", "Azərbaycanca"),
                            ("bg", "Български"),
                            ("bm", "Bamanankan"),
                            ("bn", "বাংলা"),
                            ("bs", "Bosanski"),
                            ("ca", "català"),
                            ("cs", "Čeština"),
                            ("da", "Dansk"),
                            ("de", "Deutsch"),
                            ("ee", "Èʋegbe"),
                            ("el", "Ελληνικά"),
                            ("en-US", "English"),
                            ("es", "Español"),
                            ("et", "eesti keel"),
                            ("eu", "Euskara"),
                            ("fa", "فارسی"),
                            ("fi", "suomi"),
                            ("fr", "Français"),
                            ("fy-NL", "Frysk"),
                            ("ga-IE", "Gaeilge (Éire)"),
                            ("gl", "Galego"),
                            ("gn", "Avañe'ẽ"),
                            ("gu-IN", "ગુજરાતી"),
                            ("ha", "هَرْشَن هَوْسَ"),
                            ("he", "עברית"),
                            ("hi-IN", "हिन्दी (भारत)"),
                            ("hr", "Hrvatski"),
                            ("hu", "Magyar"),
                            ("dsb", "Dolnoserbšćina"),
                            ("hsb", "Hornjoserbsce"),
                            ("id", "Bahasa Indonesia"),
                            ("ig", "Asụsụ Igbo"),
                            ("it", "Italiano"),
                            ("ja", "日本語"),
                            ("ka", "ქართული"),
                            ("km", "ខ្មែរ"),
                            ("kn", "ಕನ್ನಡ"),
                            ("ko", "한국어"),
                            ("ln", "Lingála"),
                            ("lt", "lietuvių kalba"),
                            ("mg", "Malagasy"),
                            ("mk", "Македонски"),
                            ("ml", "മലയാളം"),
                            ("ms", "Bahasa Melayu"),
                            ("ne-NP", "नेपाली"),
                            ("nl", "Nederlands"),
                            ("no", "Norsk"),
                            ("pl", "Polski"),
                            ("pt-BR", "Português (do Brasil)"),
                            ("pt-PT", "Português (Europeu)"),
                            ("ro", "română"),
                            ("ru", "Русский"),
                            ("si", "සිංහල"),
                            ("sk", "slovenčina"),
                            ("sl", "slovenščina"),
                            ("sq", "Shqip"),
                            ("sr", "Српски"),
                            ("sw", "Kiswahili"),
                            ("sv", "Svenska"),
                            ("ta", "தமிழ்"),
                            ("ta-LK", "தமிழ் (இலங்கை)"),
                            ("te", "తెలుగు"),
                            ("th", "ไทย"),
                            ("tn", "Setswana"),
                            ("tr", "Türkçe"),
                            ("uk", "Українська"),
                            ("ur", "اُردو"),
                            ("vi", "Tiếng Việt"),
                            ("wo", "Wolof"),
                            ("xh", "isiXhosa"),
                            ("yo", "èdè Yorùbá"),
                            ("zh-CN", "中文 (简体)"),
                            ("zh-TW", "正體中文 (繁體)"),
                            ("zu", "isiZulu"),
                        ],
                        default="en-US",
                        max_length=7,
                    ),
                ),
                ("taken_until", models.DateTimeField(blank=True, null=True)),
                (
                    "creator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="questions",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "last_answer",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="last_reply_in",
                        to="questions.answer",
                    ),
                ),
                (
                    "marked_as_spam_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="questions_marked_as_spam",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="questions",
                        to="products.product",
                    ),
                ),
                (
                    "solution",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="solution_for",
                        to="questions.answer",
                    ),
                ),
                (
                    "tags",
                    kitsune.tags.models.BigVocabTaggableManager(
                        help_text="A comma-separated list of tags.",
                        through="taggit.TaggedItem",
                        to="taggit.Tag",
                        verbose_name="Tags",
                    ),
                ),
                (
                    "taken_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "topic",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="questions",
                        to="products.topic",
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="questions_updated",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-updated"],
                "permissions": (
                    ("tag_question", "Can add tags to and remove tags from questions"),
                    ("change_solution", "Can change/remove the solution to a question"),
                ),
            },
            bases=(models.Model, kitsune.search.models.SearchMixin),
        ),
        migrations.AddField(
            model_name="answer",
            name="question",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="answers",
                to="questions.question",
            ),
        ),
        migrations.AddField(
            model_name="answer",
            name="updated_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="answers_updated",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.CreateModel(
            name="AnswerVote",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("helpful", models.BooleanField(default=False)),
                ("created", models.DateTimeField(db_index=True, default=datetime.datetime.now)),
                ("anonymous_id", models.CharField(db_index=True, max_length=40)),
                (
                    "answer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="votes",
                        to="questions.answer",
                    ),
                ),
                (
                    "creator",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="answer_votes",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="QuestionVisits",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("visits", models.IntegerField(db_index=True)),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="questions.question",
                        unique=True,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="QuestionVote",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("created", models.DateTimeField(db_index=True, default=datetime.datetime.now)),
                ("anonymous_id", models.CharField(db_index=True, max_length=40)),
                (
                    "creator",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="question_votes",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="votes",
                        to="questions.question",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="VoteMetadata",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("object_id", models.PositiveIntegerField(blank=True, null=True)),
                ("key", models.CharField(db_index=True, max_length=40)),
                ("value", models.CharField(max_length=1000)),
                (
                    "content_type",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="contenttypes.contenttype",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="QuestionMetaData",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("name", models.SlugField()),
                ("value", models.TextField()),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="metadata_set",
                        to="questions.question",
                    ),
                ),
            ],
            options={
                "unique_together": {("question", "name")},
            },
        ),
        migrations.CreateModel(
            name="QuestionLocale",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "locale",
                    kitsune.sumo.models.LocaleField(
                        choices=[
                            ("af", "Afrikaans"),
                            ("ar", "Arabic"),
                            ("az", "Azerbaijani"),
                            ("bg", "Bulgarian"),
                            ("bm", "Bambara"),
                            ("bn", "Bengali"),
                            ("bs", "Bosnian"),
                            ("ca", "Catalan"),
                            ("cs", "Czech"),
                            ("da", "Danish"),
                            ("de", "German"),
                            ("ee", "Ewe"),
                            ("el", "Greek"),
                            ("en-US", "English"),
                            ("es", "Spanish"),
                            ("et", "Estonian"),
                            ("eu", "Basque"),
                            ("fa", "Persian"),
                            ("fi", "Finnish"),
                            ("fr", "French"),
                            ("fy-NL", "Frisian"),
                            ("ga-IE", "Irish (Ireland)"),
                            ("gl", "Galician"),
                            ("gn", "Guarani"),
                            ("gu-IN", "Gujarati"),
                            ("ha", "Hausa"),
                            ("he", "Hebrew"),
                            ("hi-IN", "Hindi (India)"),
                            ("hr", "Croatian"),
                            ("hu", "Hungarian"),
                            ("dsb", "Lower Sorbian"),
                            ("hsb", "Upper Sorbian"),
                            ("id", "Indonesian"),
                            ("ig", "Igbo"),
                            ("it", "Italian"),
                            ("ja", "Japanese"),
                            ("ka", "Georgian"),
                            ("km", "Khmer"),
                            ("kn", "Kannada"),
                            ("ko", "Korean"),
                            ("ln", "Lingala"),
                            ("lt", "Lithuanian"),
                            ("mg", "Malagasy"),
                            ("mk", "Macedonian"),
                            ("ml", "Malayalam"),
                            ("ms", "Malay"),
                            ("ne-NP", "Nepali"),
                            ("nl", "Dutch"),
                            ("no", "Norwegian"),
                            ("pl", "Polish"),
                            ("pt-BR", "Portuguese (Brazilian)"),
                            ("pt-PT", "Portuguese (Portugal)"),
                            ("ro", "Romanian"),
                            ("ru", "Russian"),
                            ("si", "Sinhala"),
                            ("sk", "Slovak"),
                            ("sl", "Slovenian"),
                            ("sq", "Albanian"),
                            ("sr", "Serbian"),
                            ("sw", "Swahili"),
                            ("sv", "Swedish"),
                            ("ta", "Tamil"),
                            ("ta-LK", "Tamil (Sri Lanka)"),
                            ("te", "Telugu"),
                            ("th", "Thai"),
                            ("tn", "Tswana"),
                            ("tr", "Turkish"),
                            ("uk", "Ukrainian"),
                            ("ur", "Urdu"),
                            ("vi", "Vietnamese"),
                            ("wo", "Wolof"),
                            ("xh", "Xhosa"),
                            ("yo", "Yoruba"),
                            ("zh-CN", "Chinese (Simplified)"),
                            ("zh-TW", "Chinese (Traditional)"),
                            ("zu", "Zulu"),
                        ],
                        default="en-US",
                        max_length=7,
                        unique=True,
                    ),
                ),
                (
                    "products",
                    models.ManyToManyField(
                        related_name="questions_locales", to="products.product"
                    ),
                ),
            ],
            options={
                "verbose_name": "AAQ enabled locale",
            },
        ),
        migrations.CreateModel(
            name="AAQConfig",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("pinned_articles", models.ManyToManyField(to="wiki.document")),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="aaq_configs",
                        to="products.product",
                    ),
                ),
            ],
            options={
                "verbose_name": "AAQ configuration",
            },
        ),
    ]