BEGIN TRANSACTION;

CREATE TABLE PriceHistory(
RelativeTimeStamp integer
TimeStampStr text
CurrencyCode text,
Price real
);

COMMIT;


