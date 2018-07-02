BEGIN TRANSACTION;

CREATE TABLE IF NOT EXISTS PriceHistory(
Exchange text,
RelativeTimeStamp integer,
TimeStampStr text,
CurrencyCode text,
Price real
);

COMMIT;


