# -*- encoding: utf-8 -*-

"""
    Test de creation du model de la base de donnees
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):
    """ Classe pour test pour tester les modeles de la BD """


    def setUp(self):
        """
            Nettoyer la base de données avant chaque test,
        """
        get_user_model().objects.all().delete()


    def test_create_user_with_infos_successful(self):
        """
        Test de création d'un utilisateur avec les informations réussie
        """

        login = 'john_doe'
        role_id = 1
        avatar = 'avatar.jpg'
        nom = 'Doe'
        prenoms = 'John'
        organisation = 'XYZ Corp'
        telephone = '+1234567890'
        fonction = 'Manager'
        consentement = 'Yes'
        email = 'test@example.com'
        password = 'mptestuser123'

        user = get_user_model().objects.create_user(
            login=login,
            role_id=role_id,
            avatar=avatar,
            nom=nom,
            prenoms=prenoms,
            organisation=organisation,
            telephone=telephone,
            email=email,
            fonction=fonction,
            consentement=consentement,
            password=password,
        )

        self.assertEqual(user.login, login)
        self.assertEqual(user.role_id, role_id)
        self.assertEqual(user.avatar, avatar)
        self.assertEqual(user.nom, nom)
        self.assertEqual(user.prenoms, prenoms)
        self.assertEqual(user.organisation, organisation)
        self.assertEqual(user.telephone, telephone)
        self.assertEqual(user.fonction, fonction)
        self.assertEqual(user.consentement, consentement)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))


    def test_new_user_email_normalized(self):
        """Teste si l'e-mail est normalisé pour les nouveaux utilisateurs."""
        # Échantillon d'e-mails avec leurs versions normalisées attendues

        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.com', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com'],
        ]

        # Parcourt chaque paire email/attendu dans l'échantillon
        for email, expected in sample_emails:
            # Crée un nouvel utilisateur avec l'e-mail donné et un mot de passe factice
            # user = get_user_model().objects.create_user(email, 'sample12883')
            # supprimer les information de la bd avant le test
            get_user_model().objects.all().delete()

            user = get_user_model().objects.create_user(
                email=email,
                login='sample1230',
                role_id=1,
                avatar='avatar.jpg',
                nom='Doe',
                prenoms='John',
                organisation='XYZ Corp',
                telephone='+1234567890',
                fonction='Manager',
                consentement='Yes',
                is_active=True,
                is_staff=False,
                password='mptestuser123',
            )
            # Vérifie si l'e-mail de l'utilisateur nouvellement créé est normalisé comme prévu
            self.assertEqual(user.email, expected)


    def test_new_user_without_email_raises_error(self):
        """Teste si la création d'un utilisateur sans e-mail génère une erreur de ValueError."""
        # Utilise un gestionnaire de contexte pour vérifier si une ValueError est levée
        with self.assertRaises(ValueError):
            # Tente de créer un utilisateur avec un e-mail vide et un mot de passe factice
            get_user_model().objects.create_user('', 'test123')


    def test_create_superuser(self):
        """
        Test de création d'un super utilisateur (admin) avec les informations réussie
        """

        login = 'john_doe'
        role_id = 1
        avatar = 'avatar.jpg'
        nom = 'Doe'
        prenoms = 'John'
        organisation = 'XYZ Corp'
        telephone = '+1234567890'
        fonction = 'Manager'
        consentement = 'Yes'
        email = 'test@example.com'
        password = 'mptestuser123'

        user = get_user_model().objects.create_superuser(
            login=login,
            role_id=role_id,
            avatar=avatar,
            nom=nom,
            prenoms=prenoms,
            organisation=organisation,
            telephone=telephone,
            email=email,
            fonction=fonction,
            consentement=consentement,
            password=password,
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)







