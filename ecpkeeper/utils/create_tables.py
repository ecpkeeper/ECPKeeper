import sqlite3

conn = sqlite3.connect('../var/ecpkeeper.db')


class CreateTable:
    @staticmethod
    def setup():    
        c = conn.cursor()

        create_category_table(c)
        create_footprint_categories_table(c)
        create_footprint_table(c)
        create_distributors_table(c)
        create_manufacturers_table(c)
        create_attachments_table(c)
        create_si_prefixes_table(c)
        create_units_table(c)
        create_unit_si_prefixes_table(c)
        create_measurement_units_table(c)
        create_storage_location_categories_table(c)
        create_storage_locations_table(c)
        create_parameters_table(c)
        create_parts_table(c)
        create_stock_history_table(c)
        create_part_parameters_table(c)
        create_projects_table(c)
        create_project_parts_table(c)
        create_project_attachments_table(c)
        create_part_distributors_table(c)
        create_part_manufacturers_table(c)
        conn.close()


def create_category_table(c):
    with conn:
        c.execute("CREATE TABLE IF NOT EXISTS [Category] ( \
                [Id] INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, \
                [ParentId] INTEGER, \
                [Name] NVARCHAR(64) NOT NULL, \
                [Description] NVARCHAR(64) NOT NULL, \
                [DateCreated] TIMESTAMP DEFAULT CURRENT_TIMESTAMP, \
                [DateModified] TIMESTAMP, \
                FOREIGN KEY(ParentId) REFERENCES Category(Id))")
    print("create_category_table ran successfully.")


def create_footprint_categories_table(c):
    with conn:
        c.execute('CREATE TABLE IF NOT EXISTS [FootPrintCategory] ( \
            [Id] INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, \
            [ParentId] INTEGER \
            [Name] NVARCHAR(64) NOT NULL, \
            [Description] NVARCHAR(64) NOT NULL, \
            [DateCreated] TIMESTAMP DEFAULT CURRENT_TIMESTAMP, \
            [DateModified] TIMESTAMP, \
            FOREIGN KEY(ParentId) REFERENCES FootPrintCategory(Id))')
    print("create_footprint_categories_table ran successfully.")


def create_footprint_table(c):
    with conn:
        c.execute("CREATE TABLE IF NOT EXISTS [FootPrint] ( \
                [Id] INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, \
                [Name] NVARCHAR(64) NOT NULL, \
                [Description] NVARCHAR(64) NOT NULL, \
                [ImageLocation] NVARCHAR(64) NOT NULL, \
                [FootPrintCategoryId] Integer, \
                [DateCreated] TIMESTAMP DEFAULT CURRENT_TIMESTAMP, \
                [DateModified] TIMESTAMP, \
                FOREIGN KEY(FootPrintCategoryId) REFERENCES FootPrintCategory(Id))")
    print("create_footprint_table ran successfully.")


def create_distributors_table(c):
    with conn:
        c.execute('CREATE TABLE IF NOT EXISTS [Distributor] (  \
            [Id] INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, \
            [Name] NVARCHAR(64) NOT NULL, \
            [Address] NVARCHAR(64) NOT NULL, \
            [Website] NVARCHAR(64) NOT NULL, \
            [IsPricing] BOOLEAN NOT NULL CHECK (IsPricing IN (0,1)), \
            [Email] NVARCHAR(64) NOT NULL, \
            [Phone] NVARCHAR(64) NOT NULL, \
            [Fax] NVARCHAR(64) NOT NULL, \
            [Comment] NVARCHAR(64) NOT NULL, \
            [DateCreated] TIMESTAMP DEFAULT CURRENT_TIMESTAMP, \
            [DateModified] TIMESTAMP)')
    print("create_distributors_table ran successfully.")


def create_manufacturers_table(c):
    with conn:
        c.execute('CREATE TABLE IF NOT EXISTS [Manufacturer] (  \
                [Id] INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, \
                [Name] NVARCHAR(64) NOT NULL, \
                [Address] NVARCHAR(64) NOT NULL, \
                [Website] NVARCHAR(64) NOT NULL, \
                [Email] NVARCHAR(64) NOT NULL, \
                [Phone] NVARCHAR(64) NOT NULL, \
                [Fax] NVARCHAR(64) NOT NULL, \
                [Comment] NVARCHAR(64) NOT NULL, \
                [LogoLocation] NVARCHAR(64) NOT NULL, \
                [DateCreated] TIMESTAMP DEFAULT CURRENT_TIMESTAMP, \
                [DateModified] TIMESTAMP)')
    print("create_manufacturers_table ran successfully.")


def create_attachments_table(c):
    with conn:
        c.execute('CREATE TABLE IF NOT EXISTS [Attachment] (  \
                [Id] INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, \
                [Filename] NVARCHAR(64) NOT NULL, \
                [Size] NVARCHAR(64) NOT NULL, \
                [UploadLocation] NVARCHAR(64) NOT NULL, \
                [DateCreated] TIMESTAMP DEFAULT CURRENT_TIMESTAMP, \
                [DateModified] TIMESTAMP)')
    print("create_attachments_table ran successfully.")


def create_si_prefixes_table(c):
    with conn:
        c.execute('CREATE TABLE IF NOT EXISTS [SIPrefix] (  \
                [Id] INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, \
                [Prefix] NVARCHAR(64) NOT NULL, \
                [Symbol] NVARCHAR(64) NOT NULL, \
                [Power] NVARCHAR(64) NOT NULL, \
                [DateCreated] TIMESTAMP DEFAULT CURRENT_TIMESTAMP, \
                [DateModified] TIMESTAMP)')
    print("create_si_prefixes_table ran successfully.")


def create_units_table(c):
    with conn:
        c.execute('CREATE TABLE IF NOT EXISTS [Unit] (  \
                [Id] INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, \
                [UnitName] NVARCHAR(64) NOT NULL, \
                [Symbol] NVARCHAR(64) NOT NULL, \
                [DateCreated] TIMESTAMP DEFAULT CURRENT_TIMESTAMP, \
                [DateModified] TIMESTAMP)')
    print("create_units_table ran successfully.")


def create_unit_si_prefixes_table(c):
    with conn:
        c.execute('CREATE TABLE IF NOT EXISTS [PartSIPrefix] (  \
                [Id] INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, \
                [SIPrefixId] NVARCHAR(64) NOT NULL, \
                [UnitId] NVARCHAR(64) NOT NULL, \
                [DateCreated] TIMESTAMP DEFAULT CURRENT_TIMESTAMP, \
                [DateModified] TIMESTAMP, \
                FOREIGN KEY(SIPrefixId) REFERENCES SIPrefix(Id), \
                FOREIGN KEY(UnitId) REFERENCES Unit(Id))')
    print("create_unit_si_prefixes_table ran successfully.")


def create_measurement_units_table(c):
    with conn:
        c.execute('CREATE TABLE IF NOT EXISTS [MeasurementUnit] (  \
                [Id] INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, \
                [Name] NVARCHAR(64) NOT NULL, \
                [ShortName] NVARCHAR(64) NOT NULL, \
                [DateCreated] TIMESTAMP DEFAULT CURRENT_TIMESTAMP, \
                [DateModified] TIMESTAMP)')
    print("create_measurement_units_table ran successfully.")


def create_storage_location_categories_table(c):
    with conn:
        c.execute('CREATE TABLE IF NOT EXISTS [StorageLocationCategory] (  \
                [Id] INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, \
                [ParentId] INTEGER, \
                [Name] NVARCHAR(64) NOT NULL, \
                [Description] NVARCHAR(64) NOT NULL, \
                [DateCreated] TIMESTAMP DEFAULT CURRENT_TIMESTAMP, \
                [DateModified] TIMESTAMP, \
                FOREIGN KEY(ParentId) REFERENCES StorageLocationCategory(Id))')
    print("create_storage_location_categories_table ran successfully.")


def create_storage_locations_table(c):
    with conn:
        c.execute('CREATE TABLE IF NOT EXISTS [StorageLocation] (  \
                [Id] INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, \
                [CategoryId] INTEGER, \
                [Name] NVARCHAR(64) NOT NULL, \
                [ImageLocation] NVARCHAR(64) NULL, \
                [DateCreated] TIMESTAMP DEFAULT CURRENT_TIMESTAMP, \
                [DateModified] TIMESTAMP, \
                FOREIGN KEY(CategoryId) REFERENCES StorageLocationCategory(Id))')
    print("create_storage_locations_table ran successfully.")


def create_parameters_table(c):
    with conn:
        c.execute('CREATE TABLE IF NOT EXISTS [Parameter] (  \
                [Id] INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, \
                [Name] NVARCHAR(64) NOT NULL, \
                [Description] NVARCHAR(64) NOT NULL, \
                [UnitId] INTEGER, \
                [ValueType] NVARCHAR(64) NOT NULL, \
                [Value] NVARCHAR(64) NOT NULL, \
                [MinValue] NVARCHAR(64) NOT NULL, \
                [MinValueUnit] NVARCHAR(64) NOT NULL, \
                [NominalValue] NVARCHAR(64) NOT NULL, \
                [NominalValueUnit] NVARCHAR(64) NOT NULL, \
                [MaxValue] NVARCHAR(64) NOT NULL, \
                [MaxValueUnit] NVARCHAR(64) NOT NULL, \
                [DateCreated] TIMESTAMP DEFAULT CURRENT_TIMESTAMP, \
                [DateModified] TIMESTAMP, \
                FOREIGN KEY(UnitId) REFERENCES Unit(Id))')
    print("create_parameters_table ran successfully.")


def create_parts_table(c):
    with conn:
        c.execute('CREATE TABLE IF NOT EXISTS [Part] (  \
                [Id] INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, \
                [Name] NVARCHAR(64) NOT NULL, \
                [Description] NVARCHAR(64) NOT NULL, \
                [CategoryId] INTEGER, \
                [MinimumStock] INTEGER NOT NULL, \
                [MeasurementUnitId] INTEGER NOT NULL, \
                [FootprintId] INTEGER NOT NULL, \
                [StorageLocationId] INTEGER NOT NULL, \
                [Comment] TEXT NOT NULL, \
                [ProductionRemarks] NVARCHAR(64) NOT NULL, \
                [Status] NVARCHAR(64) NOT NULL, \
                [NeedsReview] BOOLEAN NOT NULL CHECK (NeedsReview IN (0,1)), \
                [Condition] NVARCHAR(64) NOT NULL, \
                [InternalPartNumber] INTEGER NOT NULL, \
                [DateCreated] TIMESTAMP DEFAULT CURRENT_TIMESTAMP, \
                [DateModified] TIMESTAMP, \
                FOREIGN KEY(CategoryId) REFERENCES Category(Id), \
                FOREIGN KEY(MeasurementUnitId) REFERENCES MeasurementUnit(Id), \
                FOREIGN KEY(FootprintId) REFERENCES FootPrint(Id), \
                FOREIGN KEY(StorageLocationId) REFERENCES StorageLocation(Id))')
    print("create_parts_table ran successfully.")


def create_stock_history_table(c):
    with conn:
        c.execute('CREATE TABLE IF NOT EXISTS [StockHistory] (  \
                [Id] INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, \
                [PartId] INTEGER, \
                [Date] TIMESTAMP DEFAULT CURRENT_TIMESTAMP, \
                [Amount] INTEGER NULL, \
                [Price] INTEGER NULL, \
                [Comment] NVARCHAR(64) NULL, \
                FOREIGN KEY(PartId) REFERENCES Part(Id))')
    print("create_stock_history_table ran successfully.")


def create_part_parameters_table(c):
    with conn:
        c.execute('CREATE TABLE IF NOT EXISTS [PartParameter] (  \
                [Id] INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, \
                [ParameterId] INTEGER, \
                [PartId] INTEGER, \
                [DateCreated] TIMESTAMP DEFAULT CURRENT_TIMESTAMP, \
                [DateModified] TIMESTAMP, \
                FOREIGN KEY(ParameterId) REFERENCES Parameter(Id), \
                FOREIGN KEY(PartId) REFERENCES Part(Id))')
    print("create_part_parameters_table ran successfully.")


def create_projects_table(c):
    with conn:
        c.execute('CREATE TABLE IF NOT EXISTS [Project] (  \
                [Id] INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, \
                [Name] NVARCHAR(64) NOT NULL, \
                [Description] NVARCHAR(64) NOT NULL, \
                [DateCreated] TIMESTAMP DEFAULT CURRENT_TIMESTAMP, \
                [DateModified] TIMESTAMP)')
    print("create_projects_table ran successfully.")


def create_project_parts_table(c):
    with conn:
        c.execute('CREATE TABLE IF NOT EXISTS [ProjectPart] (  \
                [Id] INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, \
                [ProjectId] INTEGER, \
                [Quantity] INTEGER, \
                [OverageType] NVARCHAR(64) NOT NULL, \
                [Overage] NVARCHAR(64) NOT NULL, \
                [PartId] INTEGER, \
                [Remarks] NVARCHAR(64) NOT NULL, \
                [LotNumber] NVARCHAR(64) NOT NULL, \
                [DateCreated] TIMESTAMP DEFAULT CURRENT_TIMESTAMP, \
                [DateModified] TIMESTAMP, \
                FOREIGN KEY(ProjectId) REFERENCES Project(Id), \
                FOREIGN KEY(PartId) REFERENCES Part(Id))')
    print("create_project_parts_table ran successfully.")


def create_project_attachments_table(c):
    with conn:
        c.execute('CREATE TABLE IF NOT EXISTS [ProjectAttachment] (  \
                [Id] INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, \
                [ProjectId] INTEGER, \
                [AttachmentId] INTEGER, \
                [Description] NVARCHAR(64) NOT NULL, \
                [DateCreated] TIMESTAMP DEFAULT CURRENT_TIMESTAMP, \
                [DateModified] TIMESTAMP, \
                FOREIGN KEY(ProjectId) REFERENCES Project(Id), \
                FOREIGN KEY(AttachmentId) REFERENCES Attachment(Id))')
    print("create_project_attachments_table ran successfully.")


def create_part_distributors_table(c):
    with conn:
        c.execute('CREATE TABLE IF NOT EXISTS [PartDistributor] (  \
                [Id] INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, \
                [PartId] INTEGER, \
                [DistributorId] INTEGER, \
                [OrderNumber] INTEGER, \
                [Packaging] INTEGER, \
                [PricePerUnit] INTEGER, \
                [Currency] INTEGER, \
                [PackagePrice] INTEGER, \
                [SKU] INTEGER, \
                [Pricing] INTEGER, \
                [IsIgnore] BOOLEAN NOT NULL CHECK (IsIgnore IN (0,1)), \
                [DateCreated] TIMESTAMP DEFAULT CURRENT_TIMESTAMP, \
                [DateModified] TIMESTAMP, \
                FOREIGN KEY(PartId) REFERENCES Part(Id), \
                FOREIGN KEY(DistributorId) REFERENCES Distributor(Id))')
    print("create_part_distributors_table ran successfully.")


def create_part_manufacturers_table(c):
    with conn:
        c.execute('CREATE TABLE IF NOT EXISTS [PartManufacturers] (  \
                [Id] INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, \
                [PartId] INTEGER, \
                [ManufacturerId] INTEGER, \
                [Website] NVARCHAR(64) NOT NULL, \
                [Email] NVARCHAR(64) NOT NULL, \
                [Phone] NVARCHAR(64) NOT NULL, \
                [Fax] NVARCHAR(64) NOT NULL, \
                [Comment] NVARCHAR(64) NOT NULL, \
                [LogoLocation] NVARCHAR(64) NOT NULL, \
                [DateCreated] TIMESTAMP DEFAULT CURRENT_TIMESTAMP, \
                [DateModified] TIMESTAMP, \
                FOREIGN KEY(PartId) REFERENCES Part(Id), \
                FOREIGN KEY(ManufacturerId) REFERENCES Manufacturer(Id))')
    print("create_part_manufacturers_table ran successfully.")
