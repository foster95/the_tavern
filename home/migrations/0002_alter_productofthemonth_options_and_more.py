import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
        ("products", "0002_alter_category_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="productofthemonth",
            options={"verbose_name_plural": "Product of the Month"},
        ),

        # Keep your year field addition as-is (though your choices list is "months" –
        # leaving it because it's in your existing migration history)
        migrations.AddField(
            model_name="productofthemonth",
            name="year",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (1, "January"),
                    (2, "February"),
                    (3, "March"),
                    (4, "April"),
                    (5, "May"),
                    (6, "June"),
                    (7, "July"),
                    (8, "August"),
                    (9, "September"),
                    (10, "October"),
                    (11, "November"),
                    (12, "December"),
                ],
                default=2026,
            ),
            preserve_default=False,
        ),

        # ---- SAFE month conversion (date -> int) ----
        # 1) temp integer field
        migrations.AddField(
            model_name="productofthemonth",
            name="month_int",
            field=models.PositiveIntegerField(null=True, blank=True),
        ),

        # 2) populate month_int from old month DATE column
        migrations.RunSQL(
            sql="""
                UPDATE home_productofthemonth
                SET month_int = EXTRACT(MONTH FROM month)::int
            """,
            reverse_sql=migrations.RunSQL.noop,
        ),

        # 3) drop old month column (was DateField)
        migrations.RemoveField(
            model_name="productofthemonth",
            name="month",
        ),

        # 4) rename month_int -> month
        migrations.RenameField(
            model_name="productofthemonth",
            old_name="month_int",
            new_name="month",
        ),
        # ---- END SAFE month conversion ----

        migrations.AlterField(
            model_name="productofthemonth",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="products.product",
            ),
        ),
    ]
