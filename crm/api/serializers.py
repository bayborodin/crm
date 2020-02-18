from rest_framework import serializers

from leads.models import Lead


class LeadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lead
        fields = ('channel', 'source', 'inn', 'kpp', 'company_name', 'city',
                  'address', 'sale_channels', 'sale_regions', 'sale_points',
                  'web_address', 'comment', 'first_person',
                  'first_person_position', 'bank_account', 'bank_name',
                  'bank_rcbic', 'bank_corr_account', 'contact_person',
                  'contact_phone', 'contact_email')
