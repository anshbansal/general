package aseemEnums;

public enum TableName {
	STUDENT_TABLE("STUDENT_TABLE");

	private final String tableName;

	TableName(String tableName) {
		this.tableName = tableName;
	}

	public String toString() {
		return tableName;
	}
}
